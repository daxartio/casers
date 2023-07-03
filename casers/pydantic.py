from packaging import version
from pydantic import BaseModel
from pydantic import __version__ as pydantic_version_raw

from ._casers import to_camel

pydantic_version = version.parse(pydantic_version_raw)


if pydantic_version < version.parse("2.0.0"):  # pragma: no cover

    class CamelAliases(BaseModel):
        """Pydantic model that converts field names to camelCase."""

        class Config:
            allow_population_by_field_name = True
            alias_generator = to_camel

else:
    from pydantic import ConfigDict

    class CamelAliases(BaseModel):  # type: ignore
        """Pydantic model that converts field names to camelCase.

        >>> class User(CamelAliases):
        ...     first_name: str
        >>> User(first_name="John").model_dump(by_alias=True)
        {'firstName': 'John'}
        """

        model_config = ConfigDict(populate_by_name=True, alias_generator=to_camel)
