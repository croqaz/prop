# Py · dot

[![Python check](https://github.com/croqaz/dot/workflows/Python/badge.svg)](https://github.com/croqaz/dot/actions) ![Python 3.6](https://img.shields.io/badge/Python-3.6-blue.svg)

A Python library for getting a property from a nested object using a dot path.


## Usage

```py
import dot

data = {
    'k1': 'v1',
    'nested': {'x': 'y', 'int': 0, 'null': None},
    'list': [[None, True, 9]]
}

dot.get(data, 'k1')
# v1

dot.get(data, 'nested.x')
# x

dot.get(data, 'list.0.1')
# True

dot.get(data, 'list.0.-1')
# 9
```


## Installation

```sh
$ pip install git+https://github.com/croqaz/dot
```


## Similar libraries

* https://github.com/sindresorhus/dot-prop - (Node.js) Get, set, or delete a property from a nested object using a dot path
* https://github.com/jonschlinkert/get-value - (Node.js) Use property paths (`a.b.c`) to get a nested value from an object.


## License

[MIT](LICENSE) © Cristi Constantin.
