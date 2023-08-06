'''Parsed text representation.'''

from io import StringIO
from pathlib import Path
from typing import Any, Generator, cast

import attr
from tqdm import tqdm

from .default import PymorphyTagger, UDPipeSyntaxParser
from ..exception import ArgumentError, BaseSemSimException
from .filter import BaseSentenceFilter, MinLengthSentenceFilter
from ..logger import LoggerMixin, get_logger
from .parser import BaseSyntaxParser, clean_text, extract_text, split_conllu_into_tokens
from .tree import BaseEmbeddingModel, BaseMorphTagger, BaseStaticEmbeddingModel, Tree


__all__ = (
    'TextEngine',
    'TextRepr',
)


logger = get_logger(__name__)


@attr.s(slots=True, kw_only=True, init=False, repr=False)
class TextRepr(LoggerMixin):
    '''Text representation as a list of trees (one per sentence).'''

    text: str = attr.ib()
    trees: list[Tree] = attr.ib()

    def __init__(
        self,
        text: str,
        syntax_parser: BaseSyntaxParser,
        morph_tagger: BaseMorphTagger,
        emb_model: BaseEmbeddingModel,
        sentence_filter: BaseSentenceFilter,
        *,
        verbose: bool = True,
    ):
        '''
        Representation initialization using a bunch of models.

        :param text: a text to represent
        :param syntax_parser: syntax model to obtain CoNLL-U data and split the text into sentences and tokens
        :param morph_tagger: morphological tagger to restore MorphTag nodes' data
        :param emb_model: embedding model to use for restoring word embeddings at each node
        :param sentence_filter: sentence filter for throwing trash sentences away (e.g. too short ones)
        :param verbose: verbosity flag
        '''

        LoggerMixin.__init__(self, verbose=verbose, logger=logger)

        text = clean_text(text)
        conllu = syntax_parser.parse_text(text)
        conllu_sentences = list(filter(
            sentence_filter.is_proper,
            conllu.strip().split('\n\n'),
        ))

        if emb_model.is_static():
            self.log('Constructing trees...')
            trees = [
                Tree.from_conllu(
                    sentence,
                    morph_tagger,
                    static_emb_model=cast(BaseStaticEmbeddingModel, emb_model),
                )
                for sentence in tqdm(
                    conllu_sentences,
                    desc='Tree construction',
                    total=len(conllu_sentences),
                    disable=not verbose,
                )
            ]
        elif emb_model.is_contextual():
            tokens = split_conllu_into_tokens(conllu, verbose=verbose)
            all_embs = emb_model.process_batch(tokens)

            self.log('Constructing trees...')
            trees = [
                Tree.from_conllu(sentence, morph_tagger, embs=embs)
                for sentence, embs in tqdm(
                    zip(conllu_sentences, all_embs),
                    desc='Tree construction',
                    total=len(conllu_sentences),
                    disable=not verbose,
                )
            ]
        else:
            raise ArgumentError(
                'Parameter "emb_model" should be an instance of either '
                'BaseStaticEmbeddingModel, BaseContextualEmbeddingModel '
                'or AutoEmbeddingModel class.'
            )

        self.__attrs_init__(verbose=verbose, logger=logger, text=text, trees=trees)
        self.log('Successfully processed text.\n')

    def __getitem__(self, idx: int) -> Tree:
        return self.trees[idx]

    def __iter__(self) -> Generator[Tree, None, None]:
        yield from self.trees

    def __len__(self) -> int:
        return len(self.trees)

    def __repr__(self) -> str:
        return '\n\n'.join(
            f'Sentence #{idx}\n{tree}'
            for idx, tree in enumerate(self.trees)
        )


@attr.s(slots=True, kw_only=True, init=False)
class TextEngine(LoggerMixin):
    '''Composite model for processing texts and representing them as a list of trees.'''

    syntax_parser: BaseSyntaxParser = attr.ib()
    morph_tagger: BaseMorphTagger = attr.ib()
    emb_model: BaseEmbeddingModel = attr.ib()
    sentence_filter: BaseSentenceFilter = attr.ib(factory=MinLengthSentenceFilter)

    def __init__(self, *, verbose: bool = True, **kwargs: Any):
        '''
        Engine initialization.

        :param verbose: verbosity flag
        '''

        self.__attrs_init__(verbose=verbose, logger=logger, **kwargs)
        self.log('Successfully built TextEngine.\n')

    @syntax_parser.default
    def _(self) -> BaseSyntaxParser:
        return UDPipeSyntaxParser(verbose=self.verbose)

    @morph_tagger.default
    def _(self) -> BaseMorphTagger:
        return PymorphyTagger(verbose=self.verbose)

    @emb_model.default
    def _(self) -> BaseEmbeddingModel:
        return BaseStaticEmbeddingModel(verbose=self.verbose)

    def __attrs_post_init__(self) -> None:
        self.set_verbosity(self.verbose)

    def set_verbosity(self, verbose: bool) -> None:
        '''
        Set verbosity value.

        :param verbose: verbosity flag
        :return: None
        '''

        super().set_verbosity(verbose)
        for model in (self.syntax_parser, self.morph_tagger, self.emb_model):
            model.set_verbosity(verbose)

    def _process(self, text: str) -> TextRepr:
        return TextRepr(
            text,
            self.syntax_parser,
            self.morph_tagger,
            self.emb_model,
            self.sentence_filter,
            verbose=self.verbose,
        )

    def process(self, arg: str | StringIO | Path, is_path: bool = False) -> TextRepr:
        '''
        Process a text source and construct its representation.

        :param arg: a string, or buffer, or path to a file to be processed
        :param is_path: True if first argument is a string containing a path to a file
        :return: new TextRepr instance for the processed text
        '''

        if isinstance(arg, StringIO):
            return self._process(arg.read())
        if is_path or isinstance(arg, Path):
            try:
                text = extract_text(arg, verbose=self.verbose)
                return self._process(text)
            except BaseSemSimException:
                raise
        return self._process(arg)
