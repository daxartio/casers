from pydantic import BaseModel

from ._casers import to_camel


class CamelAliases(BaseModel):
    """Pydantic model that converts field names to camelCase.

    >>> class User(CamelAliases):
    ...     first_name: str
    >>> User(first_name="John").dict()
    {'first_name': 'John'}
    """

    class Config:
        allow_population_by_field_name = True
        alias_generator = to_camel
