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

Apple M3 Pro

```
----------------------------------------------------------------------------------------------- benchmark: 5 tests -----------------------------------------------------------------------------------------------
Name (time in us)                             Min                   Max               Mean             StdDev             Median               IQR            Outliers  OPS (Kops/s)            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_to_camel_rust                         2.4580 (1.0)         10.7919 (1.0)       2.5684 (1.0)       0.0955 (1.0)       2.5420 (1.0)      0.0410 (1.0)     2123;2123      389.3475 (1.0)       79208           1
test_to_camel_python_builtin              10.3328 (4.20)        90.1250 (8.35)     10.7271 (4.18)      0.8965 (9.39)     10.6669 (4.20)     0.2082 (5.08)    1182;1739       93.2215 (0.24)      57419           1
test_to_camel_rust_parallel               20.1249 (8.19)       102.2089 (9.47)     29.5715 (11.51)     4.0862 (42.79)    28.4170 (11.18)    4.8331 (117.94)    855;158       33.8163 (0.09)       4783           1
test_to_camel_python_builtin_parallel     36.4999 (14.85)    1,233.1251 (114.26)   39.9730 (15.56)    19.0205 (199.20)   38.1658 (15.01)    0.8328 (20.32)     95;1059       25.0169 (0.06)       8741           1
test_to_camel_pure_python                 39.4580 (16.05)      212.9169 (19.73)    40.6741 (15.84)     3.1588 (33.08)    40.2501 (15.83)    0.4161 (10.15)    614;2145       24.5857 (0.06)      21878           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
```

## License

* [MIT LICENSE](LICENSE)

## Contribution

[Contribution guidelines for this project](CONTRIBUTING.md)
