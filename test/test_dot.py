from dot import get as dot_get


def test_dot_get_list():
    assert dot_get(['asd'], '0') == 'asd'

    data = {'nested': [0, False, 'foo']}
    assert dot_get(data, 'nested.0') == 0
    assert dot_get(data, 'nested.1') is False
    assert dot_get(data, 'nested.2') == 'foo'

    assert dot_get(data, 'nested.9') is None
    assert dot_get(data, 'nested.9', 'default') == 'default'


def test_dot_get_dict():
    data = {'a': 'a', 'nested': {'x': 'y', 'int': 0, 'null': None}}
    assert dot_get(data, 'a') == 'a'
    assert dot_get(data, 'nested.x') == 'y'
    assert dot_get(data, 'nested.int') == 0
    assert dot_get(data, 'nested.null') is None

    assert dot_get(data, 'nope') is None
    assert dot_get(data, 'nope', 'default') == 'default'


def test_dot_get_obj():
    class A:
        def __init__(self, val):
            self.val = val

    a = A(1)
    assert dot_get(a, 'val') == 1
    assert dot_get(a, 'nope') is None
    assert dot_get(a, 'nope', 'default') == 'default'

    a = A([0, False, 'foo'])
    assert dot_get(a, 'val.0') == 0
    assert dot_get(a, 'val.1') is False
    assert dot_get(a, 'val.2') == 'foo'

    # from IPython import embed
    # embed(colors='linux')
