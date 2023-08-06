'''Standard (built-in) models implementation.'''

from pathlib import Path
from typing import Any, Sequence, cast
from warnings import catch_warnings, simplefilter

import attr
import pymorphy2
from simple_elmo import ElmoModel
import torch
from torch import FloatTensor
from torchwordemb import load_word2vec_text
import ufal.udpipe

from ..download import get_model_path
from ..exception import ArgumentError, FetchError, ModelError
from ..logger import get_logger
from .parser import BaseSyntaxParser
from .tag import Embedding, MorphTag
from .tree import BaseContextualEmbeddingModel, BaseEmbeddingModel, BaseMorphTagger, BaseStaticEmbeddingModel, Node


__all__ = (
    'AutoEmbeddingModel',
    'CBOWModel',
    'ELMoModel',
    'PymorphyTagger',
    'UDPipeSyntaxParser',
)


logger = get_logger(__name__)


PymorphyModel = pymorphy2.analyzer.MorphAnalyzer
UDPipeModel = ufal.udpipe.Model
UDPipeline = ufal.udpipe.Pipeline


@attr.s(slots=True, kw_only=True, init=False)
class UDPipeSyntaxParser(BaseSyntaxParser):
    '''Syntax parser model based on UDPipe.'''

    model_path: str = attr.ib(converter=str)
    model: UDPipeModel = attr.ib(repr=False)    # type: ignore
    pipeline: UDPipeline = attr.ib(repr=False)  # type: ignore

    def __init__(self, model_path: str | Path | None = None, *, verbose: bool = True):
        '''
        Parser initialization.

        :param model_path: path to a UDPipe model to load
        :param verbose: verbosity flag
        '''

        if model_path is None:
            try:
                model_path = get_model_path('udpipe')
            except FetchError:
                raise ModelError(
                    'Cannot load UDPipe model. Consider downloading '
                    'required files using "semsim.download" '
                    'or "semsim.download_all".'
                )

        model = UDPipeModel.load(str(model_path))
        if model is None:
            raise ModelError(
                'Cannot load UDPipe model. Consider downloading '
                'required files using "semsim.download" '
                'or "semsim.download_all".'
            )

        pipeline = UDPipeline(
            model,
            'tokenize',
            ufal.udpipe.Pipeline_DEFAULT_get(),
            ufal.udpipe.Pipeline_DEFAULT_get(),
            'conllu',
        )

        self.__attrs_init__(
            verbose=verbose,
            logger=logger,
            model_path=model_path,
            model=model,
            pipeline=pipeline,
        )
        self.log('Loaded UDPipe model.')

    def parse_text(self, text: str) -> str:
        '''
        Parse text and produce its CoNLL-U representation.

        :param text: text to parse
        :return: CoNLL-U representation
        '''

        self.log('Generating CoNLL-U...')
        return self.pipeline.process(text)  # type: ignore


@attr.s(slots=True, kw_only=True, init=False)
class PymorphyTagger(BaseMorphTagger):
    '''Morphological tagger based on pymorphy2.'''

    model: PymorphyModel = attr.ib(factory=PymorphyModel, init=False, repr=False)  # type: ignore

    __upos2pymorphy: dict[str, set[str]] = {
        'ADJ': {'ADJF', 'ADJS', 'COMP', 'PRTF', 'PRTS'},
        'ADP': {'PREP'},
        'ADV': {'ADVB', 'COMP'},
        'AUX': {'VERB', 'INFN'},
        'CCONJ': {'CONJ'},
        'DET': set(),
        'INTJ': {'INTJ'},
        'NOUN': {'NOUN'},
        'NUM': {'NUMR', 'NUMB', 'ROMN'},
        'PART': {'PRCL'},
        'PRON': {'PRON', 'NRPO'},
        'PROPN': {'NOUN'},
        'PUNCT': {'PNCT'},
        'SCONJ': {'CONJ'},
        'SYM': {'LATN', 'UNKN', 'PNCT', 'ROMN'},
        'VERB': {'VERB', 'INFN', 'GRND', 'PRTF', 'PRTS'},
        'X': {'LATN', 'UNKN', 'PNCT', 'ROMN'},
    }

    def __init__(self, *, verbose: bool = True):
        '''
        PymorphyTagger initialization.

        :param verbose: verbosity flag
        '''

        self.__attrs_init__(verbose=verbose, logger=logger)
        self.log('Loaded pymorphy2 model.')

    def restore_tag(self, node: Node) -> None:
        '''
        Restore MorphTag info for a given node.

        :param node: Node instance to restore tag for
        :return: None
        '''

        syntax_tag = node.tag.syntax_tag
        upos = syntax_tag.upos
        expected_tags = self.__upos2pymorphy.get(upos, set())

        parses = self.model.parse(node.token)  # type: ignore
        picked_parse = parses[0]
        for parse in parses:
            pos = parse.tag.POS
            if pos is not None and ',' in pos:
                pos = pos[:pos.index(',')]
            if pos in expected_tags:
                picked_parse = parse
                break

        node.tag.morph_tag = MorphTag(
            normal_form=picked_parse.normal_form,
            pos=picked_parse.tag.POS,
            grammemes=picked_parse.tag.grammemes,
        )


@attr.s(slots=True, kw_only=True, init=False)
class CBOWModel(BaseStaticEmbeddingModel):  # type: ignore
    '''CBOW embedding model.'''

    path: str = attr.ib(converter=str)
    default: FloatTensor | None = attr.ib(default=None, repr=False)
    vocab: dict[str, int] = attr.ib(repr=False)
    vectors: FloatTensor = attr.ib(repr=False)

    def __init__(
        self,
        path: str | Path | None = None,
        *,
        default: FloatTensor | str | None = 'mean',
        verbose: bool = True,
    ):
        '''
        CBOW embedding model initialization.

        :param path: path to CBOW dictionary and vectors
        :param default: default tensor or a strategy to produce one for missing tokens
        :param verbose: verbosity flag
        '''

        try:
            if path is None:
                path = get_model_path('cbow')
                if not path.exists():
                    raise OSError(f'Cannot load CBOW (word2vec) data from {path}')

            vocab: dict[str, int]
            vectors: FloatTensor
            vocab, vectors = load_word2vec_text(str(path))
            if not vocab:
                raise OSError(f'Cannot load CBOW (word2vec) data from {path}')

            if isinstance(default, str):
                if default == 'mean':
                    default = cast(FloatTensor, torch.mean(vectors, dim=0, dtype=torch.float))
                elif default == 'zero':
                    default = cast(FloatTensor, torch.zeros_like(vectors[0], dtype=torch.float))
                else:
                    idx = vocab.get(default)
                    if idx is None:
                        raise ArgumentError(
                            'Parameter "default" allows only the following string values: '
                            '"mean", "zero", or one of the existing vocabulary tokens.'
                        )
                    default = cast(FloatTensor, vectors[idx])

            if default is not None:
                expected_shape = vectors[0].shape
                real_shape = default.shape
                if real_shape != expected_shape:
                    raise ArgumentError(
                        'Wrong default vector shape: '
                        f'expected {expected_shape}, got {real_shape}'
                    )

            self.__attrs_init__(
                verbose=verbose,
                logger=logger,
                path=path,
                default=default,
                vocab=vocab,
                vectors=vectors,
            )
            self.log('Loaded CBOW model.')
        except (FetchError, OSError):
            raise ModelError(
                'Cannot load CBOW model. Consider downloading '
                'required files using "semsim.download" '
                'or "semsim.download_all".'
            )

    def _lookup(self, token: str) -> Embedding | None:
        idx = self.vocab.get(token)
        if idx is not None:
            return cast(Embedding, self.vectors[idx])
        if self.default is not None:
            return self.default
        return None

    def restore_embedding(self, node: Node) -> None:
        '''
        Restore static embedding for a given node.

        :param node: Node instance to restore embedding for
        :return: None
        '''

        token = f'{node.lemma}_{node.tag.syntax_tag.upos}'
        node.tag.embedding = self._lookup(token)

    @property
    def emb_size(self) -> int:
        '''Embedding dimensionality.'''

        return len(self.vectors[0])


@attr.s(slots=True, kw_only=True, init=False)
class ELMoModel(BaseContextualEmbeddingModel):  # type: ignore
    '''Contextual ELMo embedding model.'''

    emb_size: int = attr.ib()
    model: ElmoModel = attr.ib(factory=ElmoModel, repr=False)

    def __init__(self, emb_size: int = 1024, *, verbose: bool = True):
        '''
        ELMo model initialization.

        :param emb_size: supported embedding dimensionality.
        :param verbose: verbosity flag
        '''

        try:
            path = get_model_path(f'elmo{emb_size}')
            if not path.exists():
                raise OSError(f'Cannot load ELMo model from {path}')

            with catch_warnings():
                simplefilter(action='ignore', category=Warning)
                model = ElmoModel()
                model.load(str(path))

            self.__attrs_init__(verbose=verbose, logger=logger, emb_size=emb_size, model=model)
            self.log(f'Loaded ELMo-{emb_size} model.')
        except (FetchError, OSError):
            raise ModelError(
                'Cannot load ELMo model. Consider downloading '
                'required files using "semsim.download" '
                'or "semsim.download_all".'
            )

    def process_sentence(self, tokens: list[str]) -> Sequence[Embedding]:
        '''
        Produce embeddings for a list of tokens.

        :param tokens: list of tokens to produce embeddings for
        :return: sequence of embeddings, one per each token
        '''

        self.log('Generating sentence embeddings...')
        return self.process_batch([tokens])[0]

    def process_batch(self, tokens: list[list[str]]) -> Sequence[Sequence[Embedding]]:
        '''
        Produce embeddings for tokens, given a list of sentences split into tokens.

        :param tokens: list of lists of tokens, one list per sentence
        :return: sequence of embedding sequences, one sequence per sentence
        '''

        self.log('Generating batch embeddings...')
        with catch_warnings():
            simplefilter(action='ignore', category=Warning)
            vectors = self.model.get_elmo_vectors(tokens)
        return cast(Sequence[Sequence[Embedding]], vectors)


@attr.s(slots=True, kw_only=True, init=False)
class AutoEmbeddingModel(BaseEmbeddingModel):  # type: ignore
    '''Facade model for automatically instantiating an embedding model of any kind.'''

    embs_type: str | None = attr.ib()
    static_model: BaseStaticEmbeddingModel | None = attr.ib(repr=False)
    contextual_model: BaseContextualEmbeddingModel | None = attr.ib(repr=False)

    def __init__(
        self,
        embs_type: str | None = None,
        *,
        static_model: BaseStaticEmbeddingModel | None = None,
        contextual_model: BaseContextualEmbeddingModel | None = None,
        verbose: bool = True,
        **kwargs: Any,
    ):
        '''
        AutoEmbeddingModel initialization.

        :param embs_type: kind of embeddings to produce
        :param static_model: static embedding model to instantiate object with
        :param contextual_model: contextual embedding model to instantiate object with
        :param verbose: verbosity flag
        '''

        BaseEmbeddingModel.__init__(self, verbose=verbose, logger=logger)
        self.log('Detecting AutoEmbeddingModel type...')

        num_passed_args = sum(
            arg is not None
            for arg in (embs_type, static_model, contextual_model)
        )
        if num_passed_args > 1:
            raise ArgumentError(
                'You should specify at most one of "embs_type", "static_model" '
                'and "contextual_model" parameters.'
            )

        if static_model is not None:
            embs_type = 'custom_static_model'
        elif contextual_model is not None:
            embs_type = 'custom_contextual_model'
        elif embs_type is None:
            self.log(
                'Setting default AutoEmbeddingModel type to None. '
                'Make sure not to forget passing embedding type to AutoEmbeddingModel constructor.'
            )
        else:
            embs_type = embs_type.lower()
            if embs_type == 'cbow':
                static_model = CBOWModel(verbose=verbose, **kwargs)
            elif embs_type == 'elmo1024':
                contextual_model = ELMoModel(verbose=verbose, emb_size=1024, **kwargs)
            elif embs_type == 'elmo2048':
                contextual_model = ELMoModel(verbose=verbose, emb_size=2048, **kwargs)
            else:
                raise ArgumentError(
                    f'Unknown embedding model type: "{embs_type}".\n'
                    'Choose "cbow", "elmo1024", "elmo2048" or None.'
                )

        self.__attrs_init__(
            verbose=verbose,
            logger=logger,
            embs_type=embs_type,
            static_model=static_model,
            contextual_model=contextual_model,
        )

    def __attrs_post_init__(self) -> None:
        self.set_verbosity(self.verbose)

    def restore_embedding(self, node: Node) -> None:
        '''
        Restore static embedding for a given node.

        :param node: Node instance to restore embedding for
        :return: None
        '''

        if not self.is_static():
            raise ModelError('Cannot call "restore_embedding" on a non-static model.')
        if self.static_model is not None:
            self.static_model.restore_embedding(node)

    def process_sentence(self, tokens: list[str]) -> Sequence[Embedding]:
        '''
        Produce embeddings for a list of tokens.

        :param tokens: list of tokens to produce embeddings for
        :return: sequence of embeddings, one per each token
        '''

        if not self.is_contextual():
            raise ModelError('Cannot call "process_sentence" on a non-contextual model.')
        return self.contextual_model.process_sentence(tokens)  # type: ignore

    def process_batch(self, tokens: list[list[str]]) -> Sequence[Sequence[Embedding]]:
        '''
        Produce embeddings for tokens, given a list of sentences split into tokens.

        :param tokens: list of lists of tokens, one list per sentence
        :return: sequence of embedding sequences, one sequence per sentence
        '''

        if not self.is_contextual():
            raise ModelError('Cannot call "process_batch" on a non-contextual model.')
        return self.contextual_model.process_batch(tokens)  # type: ignore

    def set_verbosity(self, verbose: bool) -> None:
        '''
        Set verbosity value.

        :param verbose: verbosity flag
        :return: None
        '''

        super().set_verbosity(verbose)
        for model in (self.static_model, self.contextual_model):
            if model is not None:
                model.set_verbosity(verbose)

    def is_static(self) -> bool:
        '''
        Check whether a model generated static embeddings for each token.

        :return: True if model produces static vectors, False otherwise
        '''

        return self.contextual_model is None

    def is_contextual(self) -> bool:
        '''
        Check whether a model generated contextual (dynamic) embeddings for each token.

        :return: True if model produces contextual vectors, False otherwise
        '''

        return self.contextual_model is not None

    @property
    def emb_size(self) -> int:
        '''Embedding dimensionality.'''

        if self.is_static():
            return 0 if self.static_model is None else self.static_model.emb_size
        if self.is_contextual():
            return self.contextual_model.emb_size  # type: ignore
        raise ModelError('Cannot evaluate emb_size for empty AutoEmbeddingModel.')
