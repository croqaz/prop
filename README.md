# prop · py

  [![Build Status][build-image]][build-url]
  [![Python ver][python-image]][python-url]

A Python 🐍 library for getting a property from a nested object using a dot path.


## Usage

```py
import prop

data = {
    'k1': 'v1',
    'nested': {'x': 'y', 'int': 0, 'null': None},
    'list': [[None, True, 9]]
}

prop.get(data, 'k1')
# v1

prop.get(data, 'nested.x')
# x

prop.get(data, 'list.0.1')
# True

prop.get(data, 'list.0.-1')
# 9
```

Limitations: For navigating dicts, only string keys are supported.


## Installation

```sh
$ pip install git+https://github.com/croqaz/dot
```


## Similar libraries

* https://github.com/chrisinajar/py-dot-prop - (Python) Get a property from a dict or list
* https://github.com/sindresorhus/dot-prop - (Node.js) Get, set, or delete a property from a nested object using a dot path
* https://github.com/jonschlinkert/get-value - (Node.js) Use property paths (`a.b.c`) to get a nested value from an object


## License

[MIT](LICENSE) © Cristi Constantin.


[pypi-image]: https://img.shields.io/pypi/v/prop.svg
[pypi-url]: https://pypi.org/project/prop/
[build-image]: https://github.com/croqaz/prop/workflows/Python/badge.svg
[build-url]: https://github.com/croqaz/prop/actions
[python-image]: https://img.shields.io/badge/Python-3.6-blue.svg
[python-url]: https://python.org
