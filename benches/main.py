import re
from timeit import timeit

try:
    import plotly.graph_objects as go
except ImportError:
    go = None

from casers import to_camel, to_kebab, to_snake


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


_CONVERSION_REXP = re.compile("(.)([A-Z][a-z]+)")
_LOWER_TO_UPPER_CONVERSION_REXP = re.compile("([a-z0-9])([A-Z])")


def re_to_snake(string: str) -> str:
    s1 = _CONVERSION_REXP.sub(r"\1_\2", string)
    return _LOWER_TO_UPPER_CONVERSION_REXP.sub(r"\1_\2", s1).lower()


if __name__ == "__main__":
    number = 10000

    snake_text = "hello_world" * 100
    camel_text = "helloWorld" * 100
    results = [
        (
            timeit(lambda: to_camel(snake_text), number=number),
            "rust.to_camel",
            "red",
        ),
        (
            timeit(lambda: snake_to_camel(snake_text), number=number),
            "python.c.snake_to_camel",
            "green",
        ),
        (
            timeit(lambda: pure_py_snake_to_camel(snake_text), number=number),
            "python.pure_py_snake_to_camel",
            "blue",
        ),
        (
            timeit(lambda: to_snake(camel_text), number=number),
            "rust.to_snake",
            "red",
        ),
        (
            timeit(lambda: re_to_snake(camel_text), number=number),
            "python.re.to_snake",
            "blue",
        ),
        (
            timeit(lambda: to_kebab(camel_text), number=number),
            "rust.to_kebab",
            "red",
        ),
        (
            timeit(lambda: re_to_snake(camel_text).replace("_", "-"), number=number),
            "python.to_kebab",
            "blue",
        ),
    ]
    for res, name, _ in results:
        print(res, name)  # noqa: T201

    if go:
        x = [name for _, name, _ in results]
        y = [round(v, 2) for v, *_ in results]
        color = [c for _, _, c in results]

        fig = go.Figure(
            data=[
                go.Bar(
                    x=x,
                    y=y,
                    marker_color=color,
                    text=y,
                    textposition="auto",
                ),
            ],
        )
        fig.show()
