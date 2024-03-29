# casers

[![PyPI](https://img.shields.io/pypi/v/casers)](https://pypi.org/project/casers/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/casers)](https://www.python.org/downloads/)
[![GitHub last commit](https://img.shields.io/github/last-commit/daxartio/casers)](https://github.com/daxartio/casers)
![PyPI - Downloads](https://img.shields.io/pypi/dm/casers)
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

The package supports for pydantic 2

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

```
------------------------------------------------------------------------------------------------- benchmark: 5 tests -------------------------------------------------------------------------------------------------
Name (time in us)                              Min                   Max                Mean             StdDev              Median                IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_to_camel_rust                          6.7330 (1.0)        131.7090 (1.0)        7.4058 (1.0)       3.6480 (1.0)        6.8550 (1.0)       0.0612 (1.0)     1007;4697      135.0292 (1.0)       42768           1
test_to_camel_python_builtin               36.3011 (5.39)     1,019.0560 (7.74)      40.5981 (5.48)     14.3812 (3.94)      37.2550 (5.43)      0.5290 (8.64)     901;2044       24.6317 (0.18)      12326           1
test_to_camel_rust_parallel                72.9470 (10.83)      605.7979 (4.60)     124.9733 (16.88)    41.6080 (11.41)    113.4912 (16.56)    31.3647 (512.21)    414;199        8.0017 (0.06)       2407           1
test_to_camel_pure_python                 122.8340 (18.24)      361.8060 (2.75)     136.7272 (18.46)    30.4976 (8.36)     124.9164 (18.22)     3.6801 (60.10)    818;1421        7.3138 (0.05)       7458           1
test_to_camel_python_builtin_parallel     135.2120 (20.08)      674.6668 (5.12)     187.0079 (25.25)    61.5008 (16.86)    166.2684 (24.26)    46.5950 (760.93)    329;276        5.3474 (0.04)       2500           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
```

## License

* [MIT LICENSE](LICENSE)

## Contribution

[Contribution guidelines for this project](CONTRIBUTING.md)
