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

```
------------------------------------------------------------------------------------------------ benchmark: 5 tests ------------------------------------------------------------------------------------------------
Name (time in us)                              Min                 Max                Mean             StdDev              Median                IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_to_camel_python_builtin               31.4261 (1.0)      240.7331 (1.38)      33.6490 (1.0)       6.2544 (1.0)       32.5390 (1.0)       0.3171 (1.0)      635;2410       29.7185 (1.0)       16226           1
test_to_camel_rust                         47.2781 (1.50)     174.2220 (1.0)       49.2500 (1.46)      6.4981 (1.04)      47.7300 (1.47)      0.3830 (1.21)     656;1825       20.3046 (0.68)      12736           1
test_to_camel_pure_python                 107.1789 (3.41)     283.2729 (1.63)     114.8233 (3.41)     14.1427 (2.26)     112.8715 (3.47)      4.6182 (14.56)     418;558        8.7090 (0.29)       8522           1
test_to_camel_rust_parallel               113.6360 (3.62)     322.5910 (1.85)     145.0051 (4.31)     28.7182 (4.59)     136.9580 (4.21)     35.4961 (111.93)     302;65        6.8963 (0.23)       1917           1
test_to_camel_python_builtin_parallel     116.8901 (3.72)     392.9241 (2.26)     143.1725 (4.25)     23.2121 (3.71)     137.4620 (4.22)     23.0463 (72.67)     334;150        6.9846 (0.24)       3382           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
```

## License

* [MIT LICENSE](LICENSE)

## Contribution

[Contribution guidelines for this project](CONTRIBUTING.md)
