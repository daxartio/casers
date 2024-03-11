from pydantic import BaseModel, ConfigDict

from ._casers import to_camel


class CamelAliases(BaseModel):  # type: ignore
    """Pydantic model that converts field names to camelCase.

    >>> class User(CamelAliases):
    ...     first_name: str
    >>> User(first_name="John").model_dump(by_alias=True)
    {'firstName': 'John'}
    """

    model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
