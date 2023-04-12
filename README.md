# casers

[![PyPI](https://img.shields.io/pypi/v/casers)](https://pypi.org/project/casers/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/casers)](https://www.python.org/downloads/)
[![GitHub last commit](https://img.shields.io/github/last-commit/daxartio/casers)](https://github.com/daxartio/casers)
[![GitHub stars](https://img.shields.io/github/stars/daxartio/casers?style=social)](https://github.com/daxartio/casers)

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

```python
from casers import snake_to_camel

snake_to_camel("some_text") == "someText"
# True
```

```python
from casers.pydantic import SnakeToCamelAliases

class Model(SnakeToCamelAliases):
    snake_case: str

Model.parse_obj({"snakeCase": "value"}).snake_case == "value"
# True
```

## License

* [MIT LICENSE](LICENSE)

## Contribution

[Contribution guidelines for this project](CONTRIBUTING.md)
