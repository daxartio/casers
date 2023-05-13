import pytest

from casers import to_constant


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("some_text", "SOME_TEXT"),
        ("some text", "SOME_TEXT"),
        ("some-text", "SOME_TEXT"),
        ("someText", "SOME_TEXT"),
        ("SomeText", "SOME_TEXT"),
        ("SomeTText", "SOME_T_TEXT"),
        ("SomeTTText", "SOME_TT_TEXT"),
        ("SomeHTTP", "SOME_HTTP"),
        ("thisIsCamelCase", "THIS_IS_CAMEL_CASE"),
    ],
)
def test_to_constant(text, expected):
    assert to_constant(text) == expected
