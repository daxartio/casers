from concurrent.futures import ThreadPoolExecutor
from typing import Any

import pytest

from casers import to_camel


def snake_to_camel(string: str) -> str:
    components = string.split("_")
    return components[0] + "".join(word.title() for word in components[1:])


def pure_py_snake_to_camel(string: str) -> str:
    result = list(string)
    capitalize_next = False
    index = 0
    for char in string:
        if char == "_":
            capitalize_next = True
        else:
            if capitalize_next:
                result[index] = char.upper()
                capitalize_next = False
            else:
                result[index] = char
            index += 1
    return "".join(result)


def run_to_camel_twice(executor: ThreadPoolExecutor, func: Any, snake_text: str) -> int:
    future_1 = executor.submit(func, snake_text)
    future_2 = executor.submit(func, snake_text)
    result_1 = future_1.result()
    result_2 = future_2.result()
    return result_1 + result_2


@pytest.fixture()
def snake_text() -> str:
    return "hello_world" * 100


def test_to_camel_rust(benchmark: Any, snake_text: str) -> None:
    benchmark(to_camel, snake_text)


def test_to_camel_python_builtin(benchmark: Any, snake_text: str) -> None:
    benchmark(snake_to_camel, snake_text)


def test_to_camel_pure_python(benchmark: Any, snake_text: str) -> None:
    benchmark(pure_py_snake_to_camel, snake_text)


def test_to_camel_rust_parallel(benchmark: Any, snake_text: str) -> None:
    executor = ThreadPoolExecutor(max_workers=2)
    benchmark(run_to_camel_twice, executor, to_camel, snake_text)


def test_to_camel_python_builtin_parallel(benchmark: Any, snake_text: str) -> None:
    executor = ThreadPoolExecutor(max_workers=2)
    benchmark(run_to_camel_twice, executor, snake_to_camel, snake_text)
