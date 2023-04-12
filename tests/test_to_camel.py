import pytest

from casers import to_camel, snake_to_camel


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("some text", "someText"),
        ("some_text", "someText"),
    ],
)
def test_to_camel(text, expected):
    assert to_camel(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("some text", "some text"),
        ("some_text", "someText"),
    ],
)
def test_snake_to_camel(text, expected):
    assert snake_to_camel(text) == expected
