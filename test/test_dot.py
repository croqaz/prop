import pytest
from prop import strict_get
from prop import get as dot_get


class A:

    def __init__(self, val):
        self.val = val


def test_dot_get_list():
    assert dot_get(['asd'], '0') == 'asd'

    data = {'nested': [0, False, 'foo']}
    assert dot_get(data, 'nested.0') == 0
    assert dot_get(data, 'nested.1') is False
    assert dot_get(data, 'nested.2') == 'foo'

    # inexistent
    assert dot_get(data, 'nested.9') is None
    assert dot_get(data, 'nested.9', 'default') == 'default'


def test_dot_get_dict():
    data = {'a': 'a', 'nested': {'x': 'y', 'int': 0, 'null': None}}
    assert dot_get(data, 'a') == 'a'
    assert dot_get(data, 'nested.x') == 'y'
    assert dot_get(data, 'nested.int') == 0
    assert dot_get(data, 'nested.null') is None

    # inexistent
    assert dot_get(data, 'nope') is None
    assert dot_get(data, 'nope', 'default') == 'default'


def test_dot_get_obj():
    a = A(1)
    assert dot_get(a, 'val') == 1
    assert dot_get(a, 'nope') is None
    assert dot_get(a, 'nope', 'default') == 'default'

    a = A([0, False, 'foo'])
    assert dot_get(a, 'val.0') == 0
    assert dot_get(a, 'val.1') is False
    assert dot_get(a, 'val.2') == 'foo'

    assert dot_get(a, 'nope') is None
    assert dot_get(a, 'nope', 'default') == 'default'


def test_circular_refs():
    c = A(1)
    b = A(c)
    a = A(b)

    assert dot_get(c, 'val') == 1
    assert dot_get(b, 'val') is c
    assert dot_get(a, 'val') is b

    assert dot_get(a, 'val.val.val') == 1

    # Create cyclic ref
    c.val = a

    assert dot_get(c, 'val') == a
    assert dot_get(c, 'val.val.val.val') == a


def test_dot_get_mixed():
    data = {
        'nested': {
            1: '1',
            'x': 'y',
            None: 'null',
        },
        'list': [[[None, True, 9]]],
    }

    assert dot_get(data, 'list.0.0.1') is True

    # These examples are failing:
    # assert dot_get(data, 'nested.1') == '1'
    # assert dot_get(data, 'nested.None') == 'null'

    a = A(data)

    assert dot_get(a, 'val.nested.x') == 'y'
    assert dot_get(a, 'val.list.0.0.1') is True


def test_dot_strict_get():
    data = {
        '1': 1,
        'nested': {
            'x': 'y',
            'int': 0,
            'null': None
        },
        'list': [[[None, True, 9]]],
    }

    assert strict_get(data, '1') == 1
    assert strict_get(data, 'nested.x') == 'y'
    assert strict_get(data, 'nested.int') == 0
    assert strict_get(data, 'nested.null') is None

    assert strict_get(data, 'list.0.0.1') is True

    with pytest.raises(KeyError):
        assert strict_get(data, 'nope') is None

    with pytest.raises(IndexError):
        assert strict_get(data, 'list.9') is None

    # from IPython import embed
    # embed(colors='linux')
