'''Sentence filters.'''

from abc import ABC, abstractmethod

import attr
from attr import validators

from .parser import split_conllu_sentence_tokens


__all__ = (
    'BaseSentenceFilter',
    'IdentitySentenceFilter',
    'MinLengthSentenceFilter',
)


@attr.s(slots=True, kw_only=True)
class BaseSentenceFilter(ABC):
    '''Base class for sentence filters.'''

    @abstractmethod
    def is_proper(self, conllu_sentence: str) -> bool:
        '''
        Check whether a sentence is appropriate for being processed.

        :param conllu_sentence: CoNLL-U data for a sentence to check
        :return: True if sentence is to be processed, False otherwise
        '''

        ...


@attr.s(slots=True, kw_only=True)
class IdentitySentenceFilter(BaseSentenceFilter):
    '''Lazy filter accepting every single sentence.'''

    def is_proper(self, conllu_sentence: str) -> bool:
        '''
        Check whether a sentence is appropriate for being processed.

        :param conllu_sentence: CoNLL-U data for a sentence to check
        :return: True if sentence is to be processed, False otherwise
        '''

        return True


@attr.s(slots=True, kw_only=True)
class MinLengthSentenceFilter(BaseSentenceFilter):
    '''Filter for ignoring too short sentences with few tokens.'''

    min_length: int = attr.ib(default=4, validator=validators.gt(0))

    def is_proper(self, conllu_sentence: str) -> bool:
        '''
        Check whether a sentence is appropriate for being processed.

        :param conllu_sentence: CoNLL-U data for a sentence to check
        :return: True if sentence is to be processed, False otherwise
        '''

        tokens = split_conllu_sentence_tokens(conllu_sentence)
        return len(tokens) >= self.min_length
