# casers

[![PyPI](https://img.shields.io/pypi/v/casers)](https://pypi.org/project/casers/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/casers)](https://www.python.org/downloads/)
[![GitHub last commit](https://img.shields.io/github/last-commit/daxartio/casers)](https://github.com/daxartio/casers)
[![GitHub stars](https://img.shields.io/github/stars/daxartio/casers?style=social)](https://github.com/daxartio/casers)

## Features

| case     | example     |
|----------|-------------|
| camel    | `someText`  |
| snake    | `some_text` |
| kebab    | `some-text` |
| pascal   | `SomeText`  |
| constant | `SOME_TEXT` |

## Installation

### pip

```
pip install casers
```

### poetry

```
poetry add casers
```

## Usage

The examples are checked by pytest

```python
>>> from casers import to_camel, to_snake, to_kebab

>>> to_camel("some_text") == "someText"
True

>>> to_snake("someText") == "some_text"
True

>>> to_kebab("someText") == "some-text"
True
>>> to_kebab("some_text") == "some-text"
True

```

```python
>>> from casers.pydantic import CamelAliases

>>> class Model(CamelAliases):
...     snake_case: str

>>> Model.parse_obj({"snakeCase": "value"}).snake_case == "value"
True
>>> Model.parse_raw('{"snakeCase": "value"}').snake_case == "value"
True

```

## License

* [MIT LICENSE](LICENSE)

## Contribution

[Contribution guidelines for this project](CONTRIBUTING.md)
