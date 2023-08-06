'''Syntax parsing, CoNLL-U processing and text extraction.'''

from abc import ABC, abstractmethod
from pathlib import Path
import re
from typing import Any, Generator

import textract
from tqdm import tqdm

from ..exception import ParseError
from ..logger import LoggerMixin, get_logger


__all__ = (
    'BaseSyntaxParser',

    'clean_text',
    'extract_text',
    'split_conllu_into_lines',
    'split_conllu_into_tokens',
    'split_conllu_sentence_tokens',
)


logger = get_logger(__name__)


BAD_NON_PRINTABLE_CHARACTERS = ''.join(
    chr(idx)
    for idx in range(1, ord(' '))
    if idx not in (ord(c) for c in '\t\n')
)


def clean_text(text: str) -> str:
    '''
    Remove strange characters from text, usually produced while extracting text from pdf via OCR.

    :param text: source text to clean
    :return: clear text
    '''

    text = re.sub('[\r\n\v\f\x1c\x1d\x1e\x85\u2028\u2029]{2,}', '\n', text)
    text = re.sub(f'[{BAD_NON_PRINTABLE_CHARACTERS}]', ' ', text)
    text = re.sub('[ ]{2,}', ' ', text).strip()
    return text


def extract_text(filename: str | Path, *, verbose: bool = True) -> str:
    '''
    Extract text from a file using OCR when necessary.

    :param filename: path to a file to process
    :param verbose: verbosity flag
    :return: extracted text
    '''

    if verbose:
        logger.info(f'Extracting text from {filename}...')

    try:
        text = textract.process(filename, language='rus').decode()
        return clean_text(text)
    except Exception as exc:  # noqa
        raise ParseError(f'Text extraction failed: {exc}')


class BaseSyntaxParser(LoggerMixin, ABC):
    '''Base class for syntax parsers.'''

    def __init__(self, **kwargs: Any):
        '''Base syntax parses initialization.'''

        LoggerMixin.__init__(self, **kwargs)

    @abstractmethod
    def parse_text(self, text: str) -> str:
        '''
        Parse text and produce its CoNLL-U representation.

        :param text: text to parse
        :return: CoNLL-U representation
        '''

        ...


def split_conllu_into_lines(sentence: str) -> Generator[str, None, None]:
    '''
    Split CoNLL-U sentence data into separate lines (one per token), ignoring comments and empty lines.

    :param sentence: CoNLL-U data for a sentence
    '''

    last_line = ''
    idx = 1
    for line in sentence.strip().splitlines():
        line = line.strip()
        if not line:
            continue

        if line.startswith('#') or line.startswith(f'{idx}\t'):
            if last_line:
                yield last_line
            last_line = line
            idx += line[0].isdigit()
        else:
            last_line += f' {line}'

    if last_line:
        yield last_line


def split_conllu_sentence_tokens(sentence: str) -> list[str]:
    '''
    Get list of tokens from CoNLL-U sentence data.

    :param sentence: CoNLL-U data for a sentence
    :return: list of tokens
    '''

    tokens = []
    for line in split_conllu_into_lines(sentence):
        if not line.startswith('#'):
            _, _, token, *_ = line.split('\t')
            tokens.append(token)
    return tokens


def split_conllu_into_tokens(conllu: str, *, verbose: bool = True) -> list[list[str]]:
    '''
    Split full CoNLL-U data into tokens.

    :param conllu: full parsed CoNLL-U data
    :param verbose: verbosity flag
    :return: list of lists of tokens, one list per each sentence
    '''

    if verbose:
        logger.info('Tokenizing CoNLL-U sentences...')

    try:
        all_tokens = []
        sentences = conllu.strip().split('\n\n')
        for sentence in tqdm(sentences, desc='Sentence tokenization', total=len(sentences), disable=not verbose):
            tokens = split_conllu_sentence_tokens(sentence)
            all_tokens.append(tokens)
        return all_tokens
    except Exception as exc:
        raise ParseError(f'Sentence tokenization failed: {exc}')
