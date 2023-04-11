import pytest

from casers import to_camel


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("some text", "someText"),
    ],
)
def test_to_camel(text, expected):
    assert to_camel(text) == expected
