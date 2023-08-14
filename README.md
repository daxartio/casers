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

```
pip install casers
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

### pydantic

```
pip install "casers[pydantic]"
```

The package supports for pydantic 1 and 2 versions

```python
>>> from casers.pydantic import CamelAliases

>>> class Model(CamelAliases):
...     snake_case: str

>>> Model.model_validate({"snakeCase": "value"}).snake_case == "value"
True
>>> Model.model_validate_json('{"snakeCase": "value"}').snake_case == "value"
True

```

## Benchmark

![Benchmark](benches.png)

## License

* [MIT LICENSE](LICENSE)

## Contribution

[Contribution guidelines for this project](CONTRIBUTING.md)
