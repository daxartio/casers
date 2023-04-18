import re
from timeit import timeit
from typing import Any

from casers import to_camel, to_snake


def echo(*args: Any) -> None:
    print(*args)  # noqa: T201


def py_snake_to_camel(string: str) -> str:
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


_CONVERSION_REXP = re.compile("(.)([A-Z][a-z]+)")
_LOWER_TO_UPPER_CONVERSION_REXP = re.compile("([a-z0-9])([A-Z])")


def py_to_snake(string: str) -> str:
    s1 = _CONVERSION_REXP.sub(r"\1_\2", string)
    return _LOWER_TO_UPPER_CONVERSION_REXP.sub(r"\1_\2", s1).lower()


if __name__ == "__main__":
    number = 10000

    text = "hello_world" * 100
    echo(timeit(lambda: to_camel(text), number=number), "rust.to_camel")
    echo(
        timeit(lambda: py_snake_to_camel(text), number=number),
        "python.py_snake_to_camel",
    )
    echo(
        timeit(lambda: pure_py_snake_to_camel(text), number=number),
        "python.pure_py_snake_to_camel",
    )

    text = "helloWorld" * 100
    echo(timeit(lambda: to_snake(text), number=number), "rust.to_snake")
    echo(timeit(lambda: py_to_snake(text), number=number), "python.py_to_snake")
