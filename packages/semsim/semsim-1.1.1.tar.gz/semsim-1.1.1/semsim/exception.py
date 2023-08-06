'''SemSim exceptions.'''

__all__ = (
    'ArgumentError',
    'BaseSemSimException',
    'FetchError',
    'ModelError',
    'ParseError',
)


class BaseSemSimException(Exception):
    '''Base class for SemSim exceptions.'''

    pass


class ArgumentError(BaseSemSimException):
    '''Exception class for errors of passing wrong arguments.'''

    pass


class ModelError(BaseSemSimException):
    '''Exception class for model type errors.'''

    pass


class ParseError(BaseSemSimException):
    '''Exception class for text parsing errors.'''

    pass


class FetchError(BaseSemSimException):
    '''Exception class for errors while fetching data via HTTP GET-request.'''

    pass
