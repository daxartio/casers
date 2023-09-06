import re
from typing import Any

import pytest

from casers import to_snake

_CONVERSION_REXP = re.compile("(.)([A-Z][a-z]+)")
_LOWER_TO_UPPER_CONVERSION_REXP = re.compile("([a-z0-9])([A-Z])")


def re_to_snake(string: str) -> str:
    s1 = _CONVERSION_REXP.sub(r"\1_\2", string)
    return _LOWER_TO_UPPER_CONVERSION_REXP.sub(r"\1_\2", s1).lower()


@pytest.fixture()
def camel_text() -> str:
    return "helloWorld" * 100


def test_to_snake_rust(benchmark: Any, camel_text: str) -> None:
    benchmark(to_snake, camel_text)


def test_to_snake_python_re(benchmark: Any, camel_text: str) -> None:
    benchmark(re_to_snake, camel_text)
