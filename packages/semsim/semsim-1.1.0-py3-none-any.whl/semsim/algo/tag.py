'''Module for tree attributes (tags).'''

from collections import defaultdict

import attr
from attr import validators
from torch import FloatTensor

from .parser import split_conllu_into_lines


__all__ = (
    'DEPREL_TO_IDX',

    'Embedding',
    'MorphTag',
    'SyntaxTag',
    'Tag',

    'get_conllu_children',
    'parse_conllu',
)


DEPREL_TO_IDX = {
    'acl': 0,
    'acl:relcl': 1,
    'advcl': 2,
    'advmod': 3,
    'amod': 4,
    'appos': 5,
    'aux': 6,
    'aux:pass': 7,
    'case': 8,
    'cc': 9,
    'ccomp': 10,
    'compound': 11,
    'conj': 12,
    'cop': 13,
    'csubj': 14,
    'csubj:pass': 15,
    'dep': 16,
    'det': 17,
    'discourse': 18,
    'dislocated': 19,
    'expl': 20,
    'fixed': 21,
    'flat': 22,
    'flat:foreign': 23,
    'flat:name': 24,
    'iobj': 25,
    'list': 26,
    'mark': 27,
    'nmod': 28,
    'nsubj': 29,
    'nsubj:pass': 30,
    'nummod': 31,
    'nummod:entity': 32,
    'nummod:gov': 33,
    'obj': 34,
    'obl': 35,
    'obl:agent': 36,
    'obl:tmod': 37,
    'orphan': 38,
    'parataxis': 39,
    'punct': 40,
    'root': 41,
    'vocative': 42,
    'xcomp': 43,
}


@attr.s(slots=True, kw_only=True, init=False, eq=True, repr=False)
class SyntaxTag:
    '''Tree node tag with syntactic information extracted from CoNLL-U.'''

    idx: int = attr.ib(eq=False, validator=validators.gt(0))
    form: str = attr.ib()
    lemma: str = attr.ib()
    upos: str = attr.ib(eq=False)
    feats: dict[str, str] = attr.ib()
    head: int = attr.ib(eq=False, validator=validators.ge(0))
    deprel: str = attr.ib()
    deps: dict[int, str] = attr.ib(eq=False)
    misc: dict[str, str] = attr.ib(eq=False)

    def __init__(self, conllu_line: str):
        '''
        SyntaxTag initialization.

        :param conllu_line: one line of CoNLL-U data corresponding to the current node
        :return: None
        '''

        idx, form, lemma, upos, _, feats, head, deprel, deps, misc = conllu_line.split('\t')

        self.idx = int(idx)
        self.form = form
        self.lemma = lemma
        self.upos = upos

        self.feats = dict(
            feature.split('=') for feature in feats.split('|')
        ) if feats != '_' else {}

        self.head = int(head)
        self.deprel = deprel

        self.deps = {
            int(head): relation
            for head, relation in map(
                lambda dep: dep.split(':'),
                deps.split('|')
            )
        } if deps != '_' else {}

        self.misc = dict(
            attr.split('=') for attr in misc.split('|')
        ) if misc != '_' else {}

    def __repr__(self) -> str:
        return f'--<{self.deprel}>--> [{self.idx}] {self.form}'


def parse_conllu(conllu: str) -> dict[int, SyntaxTag]:
    '''
    Extract syntactic info from full parsed CoNLL-U data.

    :param conllu: a string containing full CoNLL-U data
    :return: mapping from node index to its syntax tag
    '''

    idx2tag = {}
    for line in split_conllu_into_lines(conllu):
        if line.startswith('#'):
            continue
        tag = SyntaxTag(line)
        idx2tag[tag.idx] = tag
    return idx2tag


def get_conllu_children(idx2tag: dict[int, SyntaxTag]) -> dict[int, list[SyntaxTag]]:
    '''
    Transpose trees to gather syntactic info about children of each node.

    :param idx2tag: mapping from node index to its syntax tag
    :return: mapping from node index to a list of syntax tags of its children
    '''

    graph = defaultdict(list)
    for idx, tag in idx2tag.items():
        graph[tag.head].append(tag)
    return graph


@attr.s(slots=True, kw_only=True)
class MorphTag:
    '''Tree node tag with morpholigical info (such as lemma, POS tag, and set of grammemes).'''

    normal_form: str = attr.ib()
    pos: str = attr.ib(default='NOUN')
    grammemes: frozenset[str] = attr.ib(factory=frozenset)

    @property
    def lemma(self) -> str:
        '''Normal form of token.'''

        return self.normal_form


Embedding = FloatTensor


@attr.s(slots=True, kw_only=True, eq=True, repr=False)
class Tag:
    '''Tree node tag with all the information about the node and its token.'''

    syntax_tag: SyntaxTag = attr.ib()
    morph_tag: MorphTag = attr.ib(default=None)
    embedding: Embedding | None = attr.ib(default=None, eq=False)

    @property
    def token(self) -> str:
        '''Initial token (before lemmatization).'''

        return self.syntax_tag.form

    @property
    def lemma(self) -> str:
        '''Normal form of token.'''

        return self.morph_tag.lemma

    @property
    def grammemes(self) -> frozenset[str]:
        '''Set of token grammemes.'''

        return self.morph_tag.grammemes

    def __repr__(self) -> str:
        return (
            f'{self.syntax_tag}' +
            f' ({self.lemma}: {self.morph_tag.pos})' +
            (' *no-emb!*' if self.embedding is None else '')
        )
