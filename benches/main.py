from timeit import timeit
from typing import Any

from casers import snake_to_camel, to_camel


def echo(*args: Any) -> None:
    print(*args)  # noqa: T201


def py_snake_to_camel(string: str) -> str:
    components = string.split("_")
    return components[0] + "".join(word.title() for word in components[1:])


if __name__ == "__main__":
    text = "hello_world" * 100
    echo(timeit(lambda: snake_to_camel(text), number=10000), "casers.snake_to_camel")
    echo(timeit(lambda: to_camel(text), number=10000), "casers.to_camel")
    echo(timeit(lambda: py_snake_to_camel(text), number=10000), "python")
