import pytest

from casers import to_kebab


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("some_text", "some-text"),
        ("some text", "some-text"),
        ("some-text", "some-text"),
        ("someText", "some-text"),
        ("SomeText", "some-text"),
        ("SomeTText", "some-t-text"),
        ("SomeTTText", "some-tt-text"),
        ("SomeHTTP", "some-http"),
        ("thisIsCamelCase", "this-is-camel-case"),
    ],
)
def test_to_kebab(text, expected):
    assert to_kebab(text) == expected
