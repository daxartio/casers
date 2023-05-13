from ._casers import to_camel, to_snake


def to_kebab(text: str) -> str:
    """Convert text to kebab-case."""
    return to_snake(text).replace("_", "-")


def to_pascal(text: str) -> str:
    """Convert text to pascal-case."""
    text = to_camel(text)
    try:
        return text[0].upper() + text[1:]
    except IndexError:
        return text


def to_constant(text: str) -> str:
    """Convert text to constant-case."""
    return to_snake(text).upper()
