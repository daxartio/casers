from ._casers import to_camel, to_snake
from ._extra import to_constant, to_kebab, to_pascal

__version__ = "0.6.1"

to_param = to_kebab

__all__ = (
    "__version__",
    "to_camel",
    "to_constant",
    "to_kebab",
    "to_param",
    "to_pascal",
    "to_snake",
)
