'''Heuristics for selecting and ordering tree pairs to be compared.'''

from abc import ABC, abstractmethod
from operator import itemgetter
from typing import Any, Generator

import attr
from attr import validators

from .kernel import jaccard_index
from ..logger import LoggerMixin, get_logger
from .representation import TextRepr
from .tree import Tree


__all__ = (
    'BaseOrderHeuristic',
    'JaccardIndexOrderHeuristic',
    'PairwiseOrderHeuristic',
)


logger = get_logger(__name__)


PairOrder = Generator[tuple[Tree, Tree], None, None]


class BaseOrderHeuristic(LoggerMixin, ABC):
    '''Base class for pair order heuristics.'''

    def __init__(self, **kwargs: Any):
        '''Base order heuristic initialization.'''

        LoggerMixin.__init__(self, **kwargs)

    @abstractmethod
    def select_pairs(self, first_repr: TextRepr, second_repr: TextRepr) -> PairOrder:
        '''
        Select and order tree pairs to be processed.

        :param first_repr: first text representation
        :param second_repr: second text representation
        '''

        ...


@attr.s(slots=True, kw_only=True, init=False)
class PairwiseOrderHeuristic(BaseOrderHeuristic):
    '''Lazy heuristic producing all possible pairs of trees.'''

    def __init__(self, *, verbose: bool = True):
        '''
        Pairwise order heuristic initialization.

        :param verbose: verbosity flag
        '''

        BaseOrderHeuristic.__init__(self, verbose=verbose, logger=logger)

    def select_pairs(self, first_repr: TextRepr, second_repr: TextRepr) -> PairOrder:
        '''
        Select and order tree pairs to be processed.

        :param first_repr: first text representation
        :param second_repr: second text representation
        '''

        self.log('Running pair selecting heuristic...')
        for lhs in first_repr:
            for rhs in second_repr:
                yield lhs, rhs


@attr.s(slots=True, kw_only=True, init=False)
class JaccardIndexOrderHeuristic(BaseOrderHeuristic):
    '''Heuristic for comparing tree pairs with large Jaccard index of their token sets.'''

    min_jaccard: float = attr.ib(validator=validators.and_(validators.ge(0), validators.le(1)))
    use_lemma: bool = attr.ib()

    def __init__(self, *, min_jaccard: float = 0, use_lemma: bool = True, verbose: bool = True):
        '''
        Jaccard order heuristic initialization.

        :param min_jaccard: min value of Jaccard index to process tree pairs
        :param use_lemma: True if lemmas are used instead of tokens for Jaccard index evaluation
        :param verbose: verbosity flag
        '''

        self.__attrs_init__(
            verbose=verbose,
            logger=logger,
            min_jaccard=min_jaccard,
            use_lemma=use_lemma,
        )

    def _compute_jaccard(self, lhs: Tree, rhs: Tree) -> float:
        left_tokens = {node.lemma if self.use_lemma else node.token for node in lhs}
        right_tokens = {node.lemma if self.use_lemma else node.token for node in rhs}
        return jaccard_index(left_tokens, right_tokens)

    def select_pairs(self, first_repr: TextRepr, second_repr: TextRepr) -> PairOrder:
        '''
        Select and order tree pairs to be processed.

        :param first_repr: first text representation
        :param second_repr: second text representation
        '''

        self.log('Running pair selecting heuristic...')
        trees = [
            (lhs, rhs, self._compute_jaccard(lhs, rhs))
            for lhs in first_repr
            for rhs in second_repr
        ]
        trees.sort(key=itemgetter(2), reverse=True)

        for lhs, rhs, jac in trees:
            if jac < self.min_jaccard:
                return
            yield (lhs, rhs)
