'''Logging utilities.'''

from abc import ABC
from logging import Formatter, Logger, StreamHandler, getLogger

import attr


__all__ = (
    'LoggerMixin',

    'get_logger',
)


LOG_FORMAT = '%(asctime)s - [%(levelname)s] - %(message)s'


def get_stream_handler(level) -> StreamHandler:  # type: ignore
    '''
    Create stream handler for logger.

    :param level: logger level of verbosity
    :return: StreamHandler instance
    '''

    stream_handler = StreamHandler()
    stream_handler.setLevel('INFO')
    stream_handler.setFormatter(Formatter(LOG_FORMAT))
    return stream_handler


def get_logger(name: str, level: str = 'INFO') -> Logger:
    '''
    Create logger.

    :param name: name of logger
    :param level: logger level of verbosity
    :return: Logger instance
    '''

    logger = getLogger(name)
    logger.setLevel(level)
    logger.addHandler(get_stream_handler(level))
    return logger


@attr.s(slots=True, kw_only=True)
class LoggerMixin(ABC):
    '''Logging mixin class.'''

    verbose: bool = attr.ib(default=True, repr=False)
    logger: Logger | None = attr.ib(default=None, repr=False)

    def log(self, text: str) -> None:
        '''
        Write portion of text in a log.

        :param text: text to log
        :return: None
        '''

        if self.verbose and self.logger is not None:
            self.logger.info(text)

    def set_verbosity(self, verbose: bool) -> None:
        '''
        Set verbosity value.

        :param verbose: verbosity flag
        :return: None
        '''

        self.verbose = verbose

    def mute(self) -> None:
        '''
        Set verbosity value to False.

        :return: None
        '''

        self.set_verbosity(False)

    def unmute(self) -> None:
        '''
        Set verbosity value to True.

        :return: None
        '''

        self.set_verbosity(True)
