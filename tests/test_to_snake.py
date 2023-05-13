import pytest

from casers import to_snake


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("some_text", "some_text"),
        ("some__text", "some_text"),
        ("some text", "some_text"),
        ("some-text", "some_text"),
        ("someText", "some_text"),
        ("SOME_TEXT", "some_text"),
        ("SomeText", "some_text"),
        ("SomeTText", "some_t_text"),
        ("SomeTTText", "some_tt_text"),
        ("SomeHTTP", "some_http"),
        ("thisIsCamelCase", "this_is_camel_case"),
    ],
)
def test_to_snake(text, expected):
    assert to_snake(text) == expected
