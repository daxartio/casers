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

Apple M4 Pro

```
---------------------------------------------------------------------------------------------- benchmark: 5 tests ---------------------------------------------------------------------------------------------
Name (time in us)                             Min                 Max               Mean            StdDev             Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_to_camel_rust                         1.5830 (1.0)       12.0830 (1.0)       1.6670 (1.0)      0.1302 (1.0)       1.6660 (1.0)      0.0010 (1.0)     643;32319      599.8728 (1.0)       97963           1
test_to_camel_python_builtin               7.3750 (4.66)      85.5000 (7.08)      7.7721 (4.66)     1.1117 (8.54)      7.6250 (4.58)     0.2080 (207.91)  1359;4023      128.6647 (0.21)      62016           1
test_to_camel_rust_parallel               15.4170 (9.74)     125.3330 (10.37)    22.6603 (13.59)    4.1499 (31.86)    21.3750 (12.83)    1.5943 (>1000.0)   754;984       44.1301 (0.07)       6265           1
test_to_camel_pure_python                 23.8750 (15.08)    108.9580 (9.02)     24.8843 (14.93)    1.3932 (10.70)    24.7920 (14.88)    0.2920 (291.87)    668;917       40.1860 (0.07)      34834           1
test_to_camel_python_builtin_parallel     30.3750 (19.19)    158.9580 (13.16)    38.7144 (23.22)    2.9676 (22.78)    38.1250 (22.88)    0.9170 (916.59)   535;1111       25.8302 (0.04)      10629           1
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
```

## License

* [MIT LICENSE](LICENSE)

## Contribution

[Contribution guidelines for this project](CONTRIBUTING.md)
