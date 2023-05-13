import pytest

from casers import to_pascal


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("Some-text", "SomeText"),
        ("some-text", "SomeText"),
        ("some text", "SomeText"),
        ("some_text", "SomeText"),
    ],
)
def test_to_pascal(text, expected):
    assert to_pascal(text) == expected
