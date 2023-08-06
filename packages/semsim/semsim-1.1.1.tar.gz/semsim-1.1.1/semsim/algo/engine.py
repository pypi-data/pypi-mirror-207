'''Main high-level class for comparing texts.'''

import heapq
from pathlib import Path
from typing import Any

import attr
from attr import validators
from tqdm import tqdm

from .heuristic import BaseOrderHeuristic, PairwiseOrderHeuristic
from .kernel import BaseKernel, TABK
from ..logger import LoggerMixin, get_logger
from .representation import TextEngine, TextRepr
from .tree import Tree


__all__ = (
    'SemSimEngine',
)


logger = get_logger(__name__)


@attr.s(slots=True, kw_only=True, order=True)
class CompareResult:
    '''Structure representing result of tree pair comparison.'''

    lhs: Tree = attr.ib(order=False)
    rhs: Tree = attr.ib(order=False)
    score: float = attr.ib(validator=[validators.ge(0), validators.le(1)])


@attr.s(slots=True, kw_only=True, init=False)
class SemSimEngine(LoggerMixin):
    '''Main class for comparing texts.'''

    engine: TextEngine = attr.ib()
    kernel: BaseKernel = attr.ib(factory=TABK)
    heuristic: BaseOrderHeuristic = attr.ib()

    max_out_pairs: int = attr.ib(default=100, validator=validators.gt(0))
    max_process_pairs: int = attr.ib(default=10_000, validator=validators.gt(0))

    def __init__(self, *, verbose: bool = True, **kwargs: Any):
        '''
        SemSimEngine initialization.

        :param verbose: verbosity flag
        '''

        self.__attrs_init__(verbose=verbose, logger=logger, **kwargs)
        self.log('Successfully built SemSimEngine.\n')

    @engine.default
    def _(self) -> TextEngine:
        return TextEngine(verbose=self.verbose)

    @heuristic.default
    def _(self) -> BaseOrderHeuristic:
        return PairwiseOrderHeuristic(verbose=self.verbose)

    def __attrs_post_init__(self) -> None:
        self.set_verbosity(self.verbose)

    def set_verbosity(self, verbose: bool) -> None:
        '''
        Set verbosity value.

        :param verbose: verbosity flag
        :return: None
        '''

        super().set_verbosity(verbose)
        for attribute in (self.engine, self.heuristic):
            attribute.set_verbosity(verbose)

    def find_top_closest(
        self,
        first_source: str | Path,
        second_source: str | Path,
    ) -> list[CompareResult]:
        '''
        Get list of top sentence pairs sorted by score (descending), given text sources.

        Needed for tests compatibility, should not be used in reliable code.
        Use `find_top_closest_sentences` instead.

        :param first_source: first text source to compare, raw text or path to a file
        :param second_source: second text source to compare, raw text or path to a file
        :return: list of CompareResult instances, one per each sentence pair
        '''

        return self.find_top_closest_sentences(first_source, second_source)

    def find_top_closest_sentences(
        self,
        first_source: str | Path,
        second_source: str | Path,
    ) -> list[CompareResult]:
        '''
        Get list of top sentence pairs sorted by score (descending), given text sources.

        :param first_source: first text source to compare, raw text or path to a file
        :param second_source: second text source to compare, raw text or path to a file
        :return: list of CompareResult instances, one per each sentence pair
        '''

        first_repr = self.engine.process(first_source)
        second_repr = self.engine.process(second_source)
        return self.find_top_closest_trees(first_repr, second_repr)

    def find_top_closest_trees(
        self,
        first_repr: TextRepr,
        second_repr: TextRepr,
    ) -> list[CompareResult]:
        '''
        Get list of top sentence pairs sorted by score (descending), given tree pairs.

        :param first_repr: first text representation
        :param second_repr: second text representation
        :return: list of CompareResult instances, one per each sentence pair
        '''

        pairs = self.heuristic.select_pairs(first_repr, second_repr)
        total_pairs = min(len(first_repr) * len(second_repr), self.max_process_pairs)
        iter_pairs = tqdm(
            pairs,
            desc='Running kernel',
            total=total_pairs,
            disable=not self.verbose,
        )

        heap: list[CompareResult] = []
        for idx, (lhs, rhs) in enumerate(iter_pairs):
            if idx == self.max_process_pairs:
                break
            sim = self.kernel.compute(lhs, rhs)
            cmp = CompareResult(lhs=lhs, rhs=rhs, score=sim)
            if len(heap) == self.max_out_pairs:
                heapq.heappushpop(heap, cmp)
            else:
                heapq.heappush(heap, cmp)
        heap.sort(reverse=True)
        return heap
