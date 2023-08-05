import math

from katalytic.data.checks import is_number, is_sequence, is_iterable, is_iterator
from katalytic.pkg import get_version

__version__, __version_info__ = get_version(__name__)
_UNDEFINED = object()


def L1(a, b):
    if isinstance(a, bool):
        raise ValueError(f'Got <a> = {a!r}')
    elif isinstance(b, bool):
        raise ValueError(f'Got <b> = {b!r}')
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(a - b)
    elif is_sequence(a) and is_sequence(b):
        if len(a) == 0 and len(b) == 0:
            raise ValueError(f'Both sequences are empty')
        elif len(a) != len(b):
            raise ValueError(f'The sequences have different lengths: {len(a)} and {len(b)}')
        elif is_sequence(a[0]) or is_sequence(b[0]):
            raise ValueError(f'Nested sequences are not supported')
        else:
            return sum(L1(ai, bi) for ai, bi in zip(a, b))
    else:
        raise ValueError(f'Unknown format: ({type(a).__name__}) {a!r} and ({type(b).__name__}) {b!r}')


def L2(a, b):
    if isinstance(a, bool):
        raise ValueError(f'Got <a> = {a!r}')
    elif isinstance(b, bool):
        raise ValueError(f'Got <b> = {b!r}')
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return math.sqrt((a - b)**2)
    elif is_sequence(a) and is_sequence(b):
        if len(a) == 0 and len(b) == 0:
            raise ValueError(f'Both sequences are empty')
        elif len(a) != len(b):
            raise ValueError(f'The sequences have different lengths: {len(a)} and {len(b)}')
        elif is_sequence(a[0]) or is_sequence(b[0]):
            raise ValueError(f'Nested sequences are not supported')
        elif any(isinstance(ai, bool) or isinstance(bi, bool) for ai, bi in zip(a, b)):
            raise ValueError(f'Got a boolean value in one of the sequences')
        elif all(isinstance(ai, (int, float)) and isinstance(bi, (int, float)) for ai, bi in zip(a, b)):
            return math.sqrt(sum((ai - bi)**2 for ai, bi in zip(a, b)))
        else:
            raise ValueError(f'Unknown format: ({type(a).__name__}) {a!r} and ({type(b).__name__}) {b!r}')
    else:
        raise ValueError(f'Unknown format: ({type(a).__name__}) {a!r} and ({type(b).__name__}) {b!r}')


def min_max(iterable, *, default=_UNDEFINED, key=None):
    if not is_iterable(iterable):
        raise TypeError(f'<iterable> expected an iterable, got {type(iterable).__name__}')
    elif not (key is None or callable(key)):
        raise TypeError(f'<key> expected a callable, got {type(key).__name__}')

    if key is None:
        key = lambda x: x

    if is_iterator(iterable):
        iterable = list(iterable)

    if len(iterable) == 0:
        if default is _UNDEFINED:
            raise ValueError(f'Cannot get the min/max of an empty iterable')
        else:
            return default

    min_ = min(iterable, key=key)
    max_ = max(iterable, key=key)
    return (min_, max_)


def clip(x, min_=float('-inf'), max_=float('+inf')):
    if not is_number(x):
        raise TypeError(f'<x> expected a number, got {type(x).__name__}')
    elif not is_number(min_):
        raise TypeError(f'<min_> expected a number, got {type(min_).__name__}')
    elif not is_number(max_):
        raise TypeError(f'<max_> expected a number, got {type(max_).__name__}')

    return min(max(x, min_), max_)
