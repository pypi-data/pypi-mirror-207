'''Tree comparison kernels implementation.'''

from abc import ABC, abstractmethod
from collections import Counter
from pathlib import Path
from typing import Any, Callable, cast

import attr
from attr import validators
import networkx as nx
from networkx.algorithms.bipartite.matching import minimum_weight_full_matching
import numpy as np
import numpy.typing as npt
from scipy.spatial.distance import (
    chebyshev, cityblock, cosine, euclidean, hamming, jaccard, minkowski,
)
import torch
from torch import nn
from torch_geometric.loader import DataLoader

from ..download import get_model_path
from ..exception import ArgumentError
from .neural import build_pyg_dataset, GAT, GCN
from .tag import DEPREL_TO_IDX, Embedding
from .tree import Node, Tree


__all__ = (
    'AdditiveKernel',
    'AssignmentKernel',
    'BaseKernel',
    'CompositeKernel',
    'MSK',
    'NeuralKernel',
    'SABK',
    'TABK',

    'jaccard_index',
)


DistSimFunction = Callable[[Embedding, Embedding], float]
DistSimMatrix = npt.NDArray[np.float32]

DEFAULT_LAMBDA = 3
DISTANCES: dict[str, DistSimFunction] = {
    'chebyshev': chebyshev,
    'cosine': cosine,
    'euclidean': euclidean,
    'hamming': hamming,
    'jaccard': jaccard,
    'manhattan': cityblock,
}


def get_similarity_func(
    func: str | DistSimFunction,
    is_distance: bool | None = None,
    is_normalized: bool | None = None,
    p: float | None = None,
) -> DistSimFunction:
    '''
    Get similarity metric for token embeddings given user-defined parameters.

    :param func: similarity/distance metric function or name of one of predefined distance metrics
    :param is_distance: True if user-defined callable `func` is distance metric, not similarity metric
    :param is_normalized: True if user-defined callable `func` returns valued from range [0; 1]
    :param p: power parameter for Minkowski distance
    :return: similarity metric function
    '''

    if isinstance(func, str):
        if is_distance is not None or is_normalized is not None:
            raise ArgumentError(
                'You cannot specify "is_distance" and "is_normalized" '
                'parameters while providing a metric name as a string.')
        if func == 'minkowski':
            if p is None:
                raise ArgumentError('Specify value of parameter "p" for Minkowski distance.')
            if p <= 0:
                raise ArgumentError('Parameter "p" should be positive.')
            return lambda x, y: 1 / (1 + minkowski(x, y, p))
        if func not in DISTANCES:
            raise ArgumentError(f'Unknown metric "{func}".')
        if p is not None:
            raise ArgumentError('Cannot specify parameter "p" for non-Minkowski distance.')

        dist = DISTANCES[func]
        if func == 'cosine':
            return lambda x, y: 1 - dist(x, y) / 2
        if func in {'jaccard', 'hamming'}:
            return lambda x, y: 1 - dist(x, y)
        return lambda x, y: 1 / (1 + dist(x, y))

    if not callable(func):
        raise ArgumentError('Parameter "func" should be either a string or callable.')

    if is_distance:
        if is_normalized:
            return cast(DistSimFunction, lambda x, y: 1 - func(x, y))
        return cast(DistSimFunction, lambda x, y: 1 / (1 + func(x, y)))
    if is_normalized is not None:
        raise ArgumentError(
            'Parameter "is_normalized" is not used '
            'for custom similarity functions.')
    return func


def build_deprel_sim_matrix(
    deprel_sim: DistSimMatrix | None = None,
    theta: float | None = None,
    lambda_: float | None = None,
) -> DistSimMatrix:
    r'''
    Construct dependency relation similarity matrix.

    :param deprel_sim: user-defined dependency relation similarity matrix
    :param theta: $\theta$ value placed on the matrix diagonal
    :param lambda_: $\lambda$ value added to the matrix diagonal
    :return: dependency relation similarity matrix
    '''

    num_deps = len(DEPREL_TO_IDX)
    if deprel_sim is not None:
        if theta is not None or lambda_ is not None:
            raise ArgumentError(
                'You should specify either "deprel_sim" or "theta" '
                'or "lambda_" parameter.')
        if deprel_sim.shape != (num_deps, num_deps):
            raise ArgumentError(
                f'Wrong shape {deprel_sim.shape} of "deprel_sim": '
                'expected {(num_deps, num_deps)}.')
        if min(deprel_sim) < 0:
            raise ArgumentError(
                'The "deprel_sim" matrix should only contain '
                'non-negative numbers.')
        return deprel_sim

    if theta is not None:
        if lambda_ is not None:
            raise ArgumentError(
                'You should specify either "theta" or "lambda_"'
                'parameter, but not both.')
        if theta < 1:
            raise ArgumentError('Parameter "theta" cannot be less than 1.')
        lambda_ = theta - 1

    if lambda_ is not None:
        if lambda_ < 0:
            raise ArgumentError('Parameter "lambda_" should be non-negative.')
    else:
        lambda_ = DEFAULT_LAMBDA

    deprel_sim = np.ones((num_deps, num_deps), dtype=float)
    deprel_sim += lambda_ * np.eye(num_deps, dtype=float)
    deprel_sim /= lambda_ + 1
    return deprel_sim


def jaccard_index(lhs: set[str] | frozenset[str], rhs: set[str] | frozenset[str]) -> float:
    '''
    Compute Jaccard similarity index for two given sets of strings.

    :param lhs: left-hand side operand, set of strings
    :param rhs: right-hand side operand, set of strings
    :return: Jaccard index
    '''

    intersection = lhs & rhs
    return len(intersection) / (len(lhs) + len(rhs) - len(intersection))


class BaseKernel(ABC):
    '''Base class for tree comparison kernels.'''

    @abstractmethod
    def compute(self, lhs: Tree, rhs: Tree) -> float:
        '''
        Compute similarity score for two given trees.

        :param lhs: left-hand side operand, attributed tree of a sentence
        :param rhs: right-hand side operand, attributed tree of a sentence
        :return: tree similarity score
        '''

        ...


@attr.s(slots=True, kw_only=True, init=False)
class BigramKernel(BaseKernel):
    '''Base class for bigram tree comparison kernels.'''

    cmp_lemma: bool = attr.ib()
    similarity_type: str = attr.ib()
    emb_similarity: DistSimFunction = attr.ib(repr=False)
    deprel_sim: DistSimMatrix = attr.ib(repr=False)

    def __init__(
        self,
        *,
        cmp_lemma: bool = True,

        emb_metric: str | DistSimFunction = 'cosine',
        is_distance: bool | None = None,
        is_normalized: bool | None = None,
        p: float | None = None,

        deprel_sim: DistSimMatrix | None = None,
        theta: float | None = None,
        lambda_: float | None = None,
    ):
        r'''
        Bigram kernel initialization.

        :param cmp_lemma: whether to compare lemmas instead of tokens in case of missing embeddings
        :param emb_metric: custom callable or name of a predefined distance metric for embeddings
        :param is_distance: True if user-defined callable `func` is distance metric, not similarity metric
        :param is_normalized: True if user-defined callable `func` returns valued from range [0; 1]
        :param p: power parameter for Minkowski distance
        :param deprel_sim: user-defined dependency relation similarity matrix
        :param theta: $\theta$ value placed on the matrix diagonal
        :param lambda_: $\lambda$ value added to the matrix diagonal
        '''

        BigramKernel.__attrs_init__(
            self,
            cmp_lemma=cmp_lemma,
            similarity_type=emb_metric if isinstance(emb_metric, str) else 'custom',
            emb_similarity=get_similarity_func(emb_metric, is_distance, is_normalized, p),
            deprel_sim=build_deprel_sim_matrix(deprel_sim, theta, lambda_),
        )


@attr.s(slots=True, kw_only=True, init=False)
class AdditiveKernel(BigramKernel, ABC):  # type: ignore[override]
    '''Base class for additive bigram kernels.'''

    gamma: float = attr.ib(validator=validators.and_(validators.gt(0), validators.le(1)))

    def __init__(self, gamma: float = 0.15, **kwargs: Any):
        r'''
        Additive kernel initialization.

        :param gamma: $\gamma$ value for post-calibrating similarity scores
        '''

        if not 0 < gamma <= 1:
            raise AttributeError('Parameter "gamma" should be in range (0; 1].')
        BigramKernel.__init__(self, **kwargs)
        self.gamma = gamma

    def compute(self, lhs: Tree, rhs: Tree) -> float:
        '''
        Compute similarity score for two given trees.

        :param lhs: left-hand side operand, attributed tree of a sentence
        :param rhs: right-hand side operand, attributed tree of a sentence
        :return: tree similarity score
        '''

        if (lhs.size == 1) ^ (rhs.size == 1):
            return 0
        if lhs == rhs:
            return 1

        self._precompute(lhs, rhs)
        sim = 0.
        for dep_left in lhs:
            if dep_left.parent is None:
                continue
            for dep_right in rhs:
                if dep_right.parent is not None:
                    sim += self._sim(dep_left, dep_right)
        denom = self._denominator(lhs, rhs)
        result = sim / denom if denom else 0
        return result ** self.gamma

    def _precompute(self, lhs: Tree, rhs: Tree) -> None:
        pass

    def _denominator(self, lhs: Tree, rhs: Tree) -> float:
        return max(1, (lhs.size - 1) * (rhs.size - 1))

    def _sim(self, lhs: Node, rhs: Node) -> float:
        sim = self._bigram_weight(lhs, rhs) * self._node_sim(lhs, rhs)
        sim += self._bigram_weight(lhs.parent, rhs.parent) * self._node_sim(lhs.parent, rhs.parent)  # type: ignore
        sim *= self._deprel_sim(lhs.deprel, rhs.deprel) / 2
        return sim

    def _bigram_weight(self, lhs: Node, rhs: Node) -> float:
        return self._node_weight(lhs) * self._node_weight(rhs)

    def _node_weight(self, node: Node, **kwargs: Any) -> float:
        return 1

    def _node_sim(self, lhs: Node, rhs: Node) -> float:
        if lhs.embedding is not None and rhs.embedding is not None:
            return self.emb_similarity(lhs.embedding, rhs.embedding)
        elif self.cmp_lemma:
            return jaccard_index(lhs.grammemes, rhs.grammemes) if lhs.lemma == rhs.lemma else 0
        else:
            return float(lhs.token.lower() == rhs.token.lower())

    def _deprel_sim(self, lhs: str, rhs: str) -> float:
        row = DEPREL_TO_IDX[lhs]
        col = DEPREL_TO_IDX[rhs]
        return self.deprel_sim[row, col]


@attr.s(slots=True, kw_only=True, init=False)
class SABK(AdditiveKernel):  # type: ignore[override]
    '''Simple approximate bigram kernel implementation.'''

    def __init__(self, **kwargs: Any):
        '''Simple approximate bigram kernel initialization.'''

        AdditiveKernel.__init__(self, **kwargs)


@attr.s(slots=True, kw_only=True, init=False)
class TABK(AdditiveKernel):  # type: ignore[override]
    '''TF-IDF based approximate bigram kernel implementation.'''

    idf: dict[str, float] = attr.ib(repr=False)
    use_lemma: bool = attr.ib()
    unknown_idf: float = attr.ib(validator=validators.ge(0))

    _lhs_tf: dict[str, int] = attr.ib(factory=dict, init=False, repr=False)
    _rhs_tf: dict[str, int] = attr.ib(factory=dict, init=False, repr=False)

    def __init__(
        self,
        *,
        idf: dict[str, float] | None = None,
        use_lemma: bool = True,
        unknown_idf: float | None = None,
        **kwargs: Any,
    ):
        '''
        TF-IDF based approximate bigram kernel initialization.

        :param idf: IDF dictionary
        :param use_lemma: whether to use lemmas instead of tokens for lookups in IDF dictionary
        :param unknown_idf: default IDF values for unknown dictionary entries
        '''

        AdditiveKernel.__init__(self, **kwargs)

        self.idf = idf or {}
        self.use_lemma = use_lemma
        if unknown_idf is None:
            unknown_idf = 1 + np.log(len(idf)) if idf else 1
        self.unknown_idf = unknown_idf

    def _precompute(self, lhs: Tree, rhs: Tree) -> None:
        self._lhs_tf = self._compute_tf(lhs)
        self._rhs_tf = self._compute_tf(rhs)

    def _compute_tf(self, tree: Tree) -> dict[str, int]:
        if self.use_lemma:
            return Counter(node.lemma for node in tree)
        return Counter(node.token.lower() for node in tree)

    def _bigram_weight(self, lhs: Node, rhs: Node) -> float:
        return self._node_weight(lhs, tf=self._lhs_tf) * self._node_weight(rhs, tf=self._rhs_tf)

    def _node_weight(self, node: Node, **kwargs: Any) -> float:
        tf: dict[str, int] = kwargs['tf']
        word = node.lemma if self.use_lemma else node.token.lower()
        return tf[word] * self.idf.get(word, self.unknown_idf)

    def _denominator(self, lhs: Tree, rhs: Tree) -> float:
        lhs_s, lhs_s_hat = self._sum_tfidf(lhs.root, tf=self._lhs_tf)
        rhs_s, rhs_s_hat = self._sum_tfidf(rhs.root, tf=self._rhs_tf)

        lhs_s -= self._node_weight(lhs.root, tf=self._lhs_tf)
        rhs_s -= self._node_weight(rhs.root, tf=self._rhs_tf)

        return 0.5 * (lhs_s * rhs_s + (lhs_s_hat - lhs_s) * (rhs_s_hat - rhs_s))

    def _sum_tfidf(self, node: Node, *, tf: dict[str, int]) -> tuple[float, float]:
        s = self._node_weight(node, tf=tf)
        s_hat = s * node.deg

        for child in node.children:
            s_child, s_hat_child = self._sum_tfidf(child, tf=tf)
            s += s_child
            s_hat += s_hat_child

        return s, s_hat


def resolve_alpha_nu(alpha: float | None, nu: float | None) -> tuple[float, float]:
    if alpha is None:
        if nu is None:
            alpha = 0.25
            nu = 1 - alpha
        elif 0 <= nu < 1:
            alpha = 1 - nu
        else:
            raise ArgumentError('Parameter "nu" should be in range [0; 1).')
    elif nu is not None:
        raise ArgumentError(
            'You should specify either "alpha" or "nu" '
            'parameter, but not both.')
    elif 0 < alpha <= 1:
        nu = 1 - alpha
    else:
        raise ArgumentError('Parameter "alpha" should be in range (0; 1].')

    return alpha, nu


@attr.s(slots=True, kw_only=True, init=False)
class MSK(AdditiveKernel):  # type: ignore[override]
    '''Matching subtree kernel implementation.'''

    alpha: float = attr.ib(validator=validators.and_(validators.ge(0), validators.lt(1)))
    nu: float = attr.ib(validator=validators.and_(validators.gt(0), validators.le(1)))

    _dp: list[list[float | None]] = attr.ib(factory=list, init=False, repr=False)

    def __init__(
        self,
        *,
        alpha: float | None = None,
        nu: float | None = None,
        **kwargs: Any,
    ):
        r'''
        Matching subtree kernel initialization.

        :param alpha: $\alpha$ parameter value, fraction of node similarity
        :param nu: $\nu$ parameter value, fraction of subtree similarity
        '''

        self.alpha, self.nu = resolve_alpha_nu(alpha, nu)
        AdditiveKernel.__init__(self, **kwargs)

    def _precompute(self, lhs: Tree, rhs: Tree) -> None:
        self._dp = [
            [None] * rhs.size for _ in range(lhs.size)
        ]

    def _sim(self, lhs: Node, rhs: Node) -> float:
        sim = self._node_sim(lhs.parent, rhs.parent)  # type: ignore
        sim *= self._deprel_sim(lhs.deprel, rhs.deprel)
        sim *= self._subtree_sim(lhs, rhs)
        return sim

    def _subtree_sim(self, lhs: Node, rhs: Node) -> float:
        lhs_idx = lhs.idx - 1
        rhs_idx = rhs.idx - 1
        sim = self._dp[lhs_idx][rhs_idx]
        if sim is not None:
            return sim

        sim = self.alpha * self._node_sim(lhs, rhs)
        if lhs.children and rhs.children:
            children_sim = 0.
            for left in lhs.children:
                for right in rhs.children:
                    dsim = self._subtree_sim(left, right)
                    children_sim += dsim * self._deprel_sim(left.deprel, right.deprel)
            children_sim /= len(lhs.children) * len(rhs.children)
            sim += self.nu * children_sim

        self._dp[lhs_idx][rhs_idx] = sim
        return sim


def resolve_beta_delta(beta: float | None, delta: float | None) -> tuple[float, float]:
    if beta is None:
        if delta is None:
            beta = 0.6
            delta = 1 - beta
        elif 0 <= delta < 1:
            beta = 1 - delta
        else:
            raise ArgumentError('Parameter "delta" should be in range [0; 1].')
    elif delta is not None:
        raise ArgumentError(
            'You should specify either "beta" or "delta" '
            'parameter, but not both.')
    elif 0 <= beta <= 1:
        delta = 1 - beta
    else:
        raise ArgumentError('Parameter "beta" should be in range [0; 1].')

    return beta, delta


@attr.s(slots=True, kw_only=True, init=False)
class CompositeKernel(BigramKernel):  # type: ignore[override]
    '''Composite kernel implementation.'''

    beta: float = attr.ib(validator=validators.and_(validators.ge(0), validators.le(1)))
    delta: float = attr.ib(validator=validators.and_(validators.ge(0), validators.le(1)))
    tabk: TABK = attr.ib()
    msk: MSK = attr.ib()

    def __init__(
        self,
        *,
        gamma: float = 0.15,

        idf: dict[str, float] | None = None,
        use_lemma: bool = True,
        unknown_idf: float | None = None,

        alpha: float | None = None,
        nu: float | None = None,

        beta: float | None = None,
        delta: float | None = None,
        **kwargs: Any,
    ):
        r'''
        Composite kernel initialization.

        :param gamma: $\gamma$ value for post-calibrating similarity scores
        :param idf: IDF dictionary
        :param use_lemma: whether to use lemmas instead of tokens for lookups in IDF dictionary
        :param unknown_idf: default IDF values for unknown dictionary entries
        :param alpha: $\alpha$ parameter value, fraction of node similarity
        :param nu: $\nu$ parameter value, fraction of subtree similarity
        :param beta: $\beta$ parameter value, fraction of TABK score
        :param delta: $\delta$ parameter value, fraction of MSK score
        '''

        BigramKernel.__init__(self, **kwargs)
        self.beta, self.delta = resolve_beta_delta(beta, delta)
        self.tabk = TABK(gamma=gamma, idf=idf or {}, use_lemma=use_lemma, unknown_idf=unknown_idf, **kwargs)
        self.msk = MSK(gamma=gamma, alpha=alpha, nu=nu, **kwargs)

    def compute(self, lhs: Tree, rhs: Tree) -> float:
        '''
        Compute similarity score for two given trees.

        :param lhs: left-hand side operand, attributed tree of a sentence
        :param rhs: right-hand side operand, attributed tree of a sentence
        :return: tree similarity score
        '''

        return self.beta * self.tabk.compute(lhs, rhs) + self.delta * self.msk.compute(lhs, rhs)


@attr.s(slots=True, kw_only=True, init=False)
class AssignmentKernel(BigramKernel):
    '''Assignment kernel based on maximum weight assignment problem.'''

    _dp: list[list[float | None]] = attr.ib(factory=list, init=False, repr=False)

    def __init__(self, **kwargs: Any):
        '''Assignment kernel initialization.'''

        BigramKernel.__init__(self, **kwargs)

    def compute(self, lhs: Tree, rhs: Tree) -> float:
        '''
        Compute similarity score for two given trees.

        :param lhs: left-hand side operand, attributed tree of a sentence
        :param rhs: right-hand side operand, attributed tree of a sentence
        :return: tree similarity score
        '''

        self._dp = [
            [None] * rhs.size for _ in range(lhs.size)
        ]
        score = self._subtree_sim(lhs.root, rhs.root)
        return score

    def _subtree_sim(self, lhs: Node, rhs: Node) -> float:
        lhs_idx = lhs.idx - 1
        rhs_idx = rhs.idx - 1
        sim = self._dp[lhs_idx][rhs_idx]
        if sim is not None:
            return sim

        if not lhs.children or not rhs.children:
            sim = self._node_sim(lhs, rhs)
        else:
            sim = self._max_assignment(lhs.children, rhs.children)
            sim /= len(lhs.children) + len(rhs.children)
            sim *= self._node_sim(lhs, rhs)

        self._dp[lhs_idx][rhs_idx] = sim
        return sim

    def _node_sim(self, lhs: Node, rhs: Node) -> float:
        if lhs.embedding is not None and rhs.embedding is not None:
            return self.emb_similarity(lhs.embedding, rhs.embedding)
        elif self.cmp_lemma:
            return jaccard_index(lhs.grammemes, rhs.grammemes) if lhs.lemma == rhs.lemma else 0
        else:
            return float(lhs.token.lower() == rhs.token.lower())

    def _deprel_sim(self, lhs: str, rhs: str) -> float:
        row = DEPREL_TO_IDX[lhs]
        col = DEPREL_TO_IDX[rhs]
        return self.deprel_sim[row, col]

    def _max_assignment(self, left_nodes: list[Node], right_nodes: list[Node]) -> float:
        top_nodes = [node.idx for node in left_nodes]
        shift = max(top_nodes)

        graph = nx.Graph()
        for lhs in left_nodes:
            for rhs in right_nodes:
                child_sim = self._subtree_sim(lhs, rhs)
                child_sim *= self._deprel_sim(lhs.deprel, rhs.deprel)
                graph.add_edge(lhs.idx, shift + rhs.idx, weight=-child_sim)

        matches = minimum_weight_full_matching(graph, top_nodes=top_nodes, weight='weight')
        score = 0
        for left in top_nodes:
            right = matches.get(left)
            if right is not None:
                score += -2 * graph[left][right]['weight']
        return score


DEFAULT_BATCH_SIZE = 64


@attr.s(slots=True, kw_only=True, init=False)
class NeuralKernel(BaseKernel):
    '''Neural kernel based on graph neural networks.'''

    model: nn.Module = attr.ib()
    device: torch.device = attr.ib(converter=torch.device)
    batch_size: int = attr.ib(validator=validators.gt(0))

    @device.default
    def _(self) -> torch.device:
        return torch.device('cpu')

    def __init__(
        self,
        *,
        model: nn.Module | None = None,
        model_path: str | Path | None = None,
        model_type: str | None = None,
        device: torch.device | str = 'cpu',
        batch_size: int = DEFAULT_BATCH_SIZE,
        **kwargs: Any,
    ):
        '''
        Neural kernel initialization.

        :param model: graph neural network model (torch_geometric)
        :param model_path: path to GNN model checkpoint
        :param model_type: type of GNN to instantiate ('gcn' or 'gat')
        :param device: device to run GNN on ('cpu', 'gpu'/'cuda', 'mps')
        :param batch_size: batch size for batched processing mode
        :param kwargs: other arguments to initialize PyTorch GNN model
        '''

        if model is not None:
            if model_path is not None or model_type is not None:
                raise ArgumentError(
                    'You cannot specify both graph NN model '
                    'and one of the parameters "model_path" and "model_type".'
                )
            device = next(model.parameters()).device
        elif model_type is not None:
            if model_type == 'gcn':
                model = GCN(**kwargs)
            elif model_type == 'gat':
                model = GAT(**kwargs)
            else:
                raise ArgumentError(f'Unknown GNN model type "{model_type}".')
            path = model_path or get_model_path(model_type)
            model.load_state_dict(torch.load(path))
        elif model_path is not None:
            raise ArgumentError(
                'You should specify "model_type" parameter to use "model_path".'
            )
        else:
            model = GCN(**kwargs)
            path = get_model_path('gcn')
            model.load_state_dict(torch.load(path))

        model.eval()
        self.__attrs_init__(
            model=model,
            device=device,
            batch_size=batch_size,
        )

    def compute_batch(self, tree_pairs: list[tuple[Tree, Tree]]) -> list[float]:
        '''
        Compute similarity score for given tree pairs.

        :param tree_pairs: list of pairs of attributed sentence trees
        :return: list of tree similarity score values
        '''

        self.model.eval()
        dataset = build_pyg_dataset(tree_pairs)
        loader = DataLoader(dataset, batch_size=self.batch_size, shuffle=False)
        predictions = []
        for batch in loader:
            y_pred = self.model(batch.to(self.device)).detach()
            predictions.extend(y_pred[:, 0])
        return predictions

    def compute(self, lhs: Tree, rhs: Tree) -> float:
        '''
        Compute similarity score for two given trees.

        :param lhs: left-hand side operand, attributed tree of a sentence
        :param rhs: right-hand side operand, attributed tree of a sentence
        :return: tree similarity score
        '''

        return self.compute_batch([(lhs, rhs)])[0]
