#import pytest
#
from src.farkle.farkle import is_farkle


def test_is_farkle():
    res = is_farkle([2, 3, 4, 3, 6, 2])
    assert res == True

    # Not a farkle: [1, 5]
    res = is_farkle([2, 1, 4, 5, 6, 2])
    assert res == False

    # Not a farkle: [3, 3, 3]
    res = is_farkle([3, 4, 3, 3, 6, 2])
    assert res == False

    # Not a farkle:
    res = is_farkle([2, 2, 3, 3, 4, 4])
    assert res == False

    # Not a farkle:
    res = is_farkle([2, 2, 4, 4, 4, 4])
    assert res == False
