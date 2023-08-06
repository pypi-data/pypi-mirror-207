'''Node and Tree classes.'''

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Generator, Sequence

import attr

from ..exception import ArgumentError, ParseError
from ..logger import LoggerMixin
from .parser import split_conllu_into_lines
from .tag import Embedding, SyntaxTag, Tag, get_conllu_children, parse_conllu


__all__ = (
    'BaseContextualEmbeddingModel',
    'BaseEmbeddingModel',
    'BaseMorphTagger',
    'BaseStaticEmbeddingModel',
    'Node',
    'Tree',
)


@attr.s(slots=True, kw_only=True, eq=True, repr=False)
class Node:
    '''Tree node with its tag, link to a parent and a list of children nodes.'''

    tag: Tag = attr.ib()
    parent: Node | None = attr.ib(default=None, eq=False)
    children: list[Node] = attr.ib(factory=list)

    @staticmethod
    def from_conllu(
        syntax_tag: SyntaxTag,
        graph: dict[int, list[SyntaxTag]],
        idx2node: dict[int, Node],
    ) -> Node:
        '''
        Node construction from syntactic data obtained from CoNLL-U.

        :param syntax_tag: syntax tag of node to build
        :param graph: mapping from node index to a list of children's syntax tags
        :param idx2node: mapping from node index to a node, updated with the current node
        :return: new Node instance
        '''

        tag = Tag(syntax_tag=syntax_tag)
        node = Node(tag=tag)
        idx = syntax_tag.idx
        idx2node[idx] = node

        node.parent = idx2node.get(syntax_tag.head)
        node.children = [
            Node.from_conllu(child_tag, graph, idx2node)
            for child_tag in graph[idx]
        ]

        return node

    @property
    def idx(self) -> int:
        '''Node index (in a 1-indexed sentence).'''

        return self.tag.syntax_tag.idx

    @property
    def token(self) -> str:
        '''Initial token (before lemmatization).'''

        return self.tag.token

    @property
    def lemma(self) -> str:
        '''Normal form of token.'''

        return self.tag.lemma

    @property
    def deprel(self) -> str:
        '''Dependency relation name.'''

        return self.tag.syntax_tag.deprel

    @property
    def grammemes(self) -> frozenset[str]:
        '''Set of token grammemes.'''

        return self.tag.grammemes

    @property
    def embedding(self) -> Embedding | None:
        '''Token embedding (if present).'''

        return self.tag.embedding

    @property
    def deg(self) -> int:
        '''Node degree in the tree.'''

        return len(self.children) + (self.parent is not None)

    def __repr__(self) -> str:
        return repr(self.tag)


@attr.s(slots=True, kw_only=True, init=False)
class BaseMorphTagger(LoggerMixin, ABC):
    '''Base class for morphological taggers.'''

    def __init__(self, **kwargs: Any):
        '''Tagger initialization.'''

        LoggerMixin.__init__(self, **kwargs)

    @abstractmethod
    def restore_tag(self, node: Node) -> None:
        '''
        Restore MorphTag info for a given node.

        :param node: Node instance to restore tag for
        :return: None
        '''

        ...


@attr.s(slots=True, kw_only=True, init=False)
class BaseEmbeddingModel(LoggerMixin, ABC):
    '''Base class for word embedding models.'''

    def __init__(self, **kwargs: Any):
        '''Embedding model initialization.'''

        LoggerMixin.__init__(self, **kwargs)

    @abstractmethod
    def restore_embedding(self, node: Node) -> None:
        '''
        Restore static embedding for a given node.

        :param node: Node instance to restore embedding for
        :return: None
        '''

        ...

    @abstractmethod
    def process_sentence(self, tokens: list[str]) -> Sequence[Embedding]:
        '''
        Produce embeddings for a list of tokens.

        :param tokens: list of tokens to produce embeddings for
        :return: sequence of embeddings, one per each token
        '''

        ...

    @abstractmethod
    def process_batch(self, tokens: list[list[str]]) -> Sequence[Sequence[Embedding]]:
        '''
        Produce embeddings for tokens, given a list of sentences split into tokens.

        :param tokens: list of lists of tokens, one list per sentence
        :return: sequence of embedding sequences, one sequence per sentence
        '''

        ...

    def is_static(self) -> bool:
        '''
        Check whether a model generated static embeddings for each token.

        :return: True if model produces static vectors, False otherwise
        '''

        return False

    def is_contextual(self) -> bool:
        '''
        Check whether a model generated contextual (dynamic) embeddings for each token.

        :return: True if model produces contextual vectors, False otherwise
        '''

        return False

    @property
    def emb_size(self) -> int:
        '''Embedding dimensionality.'''

        raise NotImplementedError


@attr.s(slots=True, kw_only=True, init=False)
class BaseStaticEmbeddingModel(BaseEmbeddingModel):
    '''Base class for static word embedding models.'''

    def __init__(self, **kwargs: Any):
        '''Static embedding model initialization.'''

        BaseEmbeddingModel.__init__(self, **kwargs)

    def restore_embedding(self, node: Node) -> None:
        '''
        Restore static embedding for a given node.

        :param node: Node instance to restore embedding for
        :return: None
        '''

        pass

    def process_sentence(self, tokens: list[str]) -> Sequence[Embedding]:
        '''
        Produce embeddings for a list of tokens.

        :param tokens: list of tokens to produce embeddings for
        :return: sequence of embeddings, one per each token
        '''

        raise NotImplementedError

    def process_batch(self, tokens: list[list[str]]) -> Sequence[Sequence[Embedding]]:
        '''
        Produce embeddings for tokens, given a list of sentences split into tokens.

        :param tokens: list of lists of tokens, one list per sentence
        :return: sequence of embedding sequences, one sequence per sentence
        '''

        raise NotImplementedError

    def is_static(self) -> bool:
        '''
        Check whether a model generated static embeddings for each token.

        :return: True if model produces static vectors, False otherwise
        '''

        return True


@attr.s(slots=True, kw_only=True, init=False)
class BaseContextualEmbeddingModel(BaseEmbeddingModel):
    '''Base class for contextual word embedding models.'''

    def __init__(self, **kwargs: Any):
        '''Contextual embedding model initialization.'''

        BaseEmbeddingModel.__init__(self, **kwargs)

    def restore_embedding(self, node: Node) -> None:
        '''
        Restore static embedding for a given node.

        :param node: Node instance to restore embedding for
        :return: None
        '''

        raise NotImplementedError

    def is_contextual(self) -> bool:
        '''
        Check whether a model generated contextual (dynamic) embeddings for each token.

        :return: True if model produces contextual vectors, False otherwise
        '''

        return True


@attr.s(slots=True, kw_only=True, eq=True, repr=False)
class Tree:
    '''Attributed syntactic (dependency) tree.'''

    root: Node = attr.ib()
    sentence: str = attr.ib(eq=False)
    idx2node: dict[int, Node] = attr.ib(factory=dict, eq=False)

    TAB_SIZE = 4

    @staticmethod
    def from_conllu(
        conllu: str,
        morph_tagger: BaseMorphTagger | None = None,
        *,
        static_emb_model: BaseEmbeddingModel | None = None,
        embs: Sequence[Embedding] | None = None,
    ) -> Tree:
        '''
        Tree construction from sentence CoNLL-U data.

        :param morph_tagger: morphological tagger
        :param static_emb_model: static embedding model
        :param embs: list of token embeddings obtained from a contextual model in advance
        :return: new Tree instance
        '''

        if static_emb_model is not None and embs is not None:
            raise ArgumentError(
                'Cannot pass both "static_emb_model" and "embs" '
                'arguments to build Tree.'
            )

        for line in split_conllu_into_lines(conllu):
            if line.startswith('# text = '):
                sentence = line[9:]
                break
        else:
            raise ParseError('Field "text" not found in CoNLL-U data.')

        idx2tag = parse_conllu(conllu)
        graph = get_conllu_children(idx2tag)
        root_tag = graph[0][0]

        idx2node: dict[int, Node] = {}
        root = Node.from_conllu(root_tag, graph, idx2node)
        tree = Tree(sentence=sentence, root=root, idx2node=idx2node)

        if morph_tagger is not None:
            tree.restore_morph_tags(morph_tagger)

        if static_emb_model is not None:
            tree.restore_static_embeddings(static_emb_model)
        elif embs is not None:
            tree.assign_contextual_embeddings(embs)
        else:
            pass

        return tree

    def restore_morph_tags(self, morph_tagger: BaseMorphTagger) -> Tree:
        '''
        Use morphological tagger to restore MorphTag node attributes.

        :param morph_tagger: morphological tagger to use
        :return: self
        '''

        for node in self.idx2node.values():
            morph_tagger.restore_tag(node)
        return self

    def restore_static_embeddings(self, static_emb_model: BaseEmbeddingModel) -> Tree:
        '''
        Use static embedding model to restore word embeddings at each node.

        :param static_emb_model: static embedding model to use
        :return: self
        '''

        for node in self.idx2node.values():
            static_emb_model.restore_embedding(node)
        return self

    def assign_contextual_embeddings(self, embs: Sequence[Embedding]) -> Tree:
        '''
        Assign (probably contextual) word embeddings for each node.

        :param embs: list of token embeddings obtained from a contextual model in advance
        :return: self
        '''

        if len(embs) != self.size:
            raise ArgumentError(
                'Wrong number of embeddings for a sentence: '
                f'expected {self.size}, get {len(embs)}'
            )

        for idx, node in self.idx2node.items():
            node.tag.embedding = embs[idx - 1]
        return self

    def __iter__(self) -> Generator[Node, None, None]:
        yield from self.idx2node.values()

    def __getitem__(self, idx: int) -> Node:
        try:
            return self.idx2node[idx]
        except KeyError:
            raise IndexError(f'No such node with index {idx} in the tree.')

    def __repr__(self) -> str:
        return f'Tree({self.sentence})'

    def pprint(self) -> None:
        '''
        Pretty printing (is it?).

        :return: None
        '''

        traversed = self._traverse(self.root)
        print(f'{self}:\n{traversed}')

    @staticmethod
    def _traverse(node: Node, depth: int = 0) -> str:
        return (
            ' ' * Tree.TAB_SIZE * depth +
            str(node) +
            ('\n' if node.children else '') +
            '\n'.join(
                Tree._traverse(child, depth + 1)
                for child in node.children
            )
        )

    @property
    def size(self) -> int:
        '''Number of vertices in a tree.'''

        return len(self.idx2node)
