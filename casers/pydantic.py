from pydantic import BaseModel

from ._casers import snake_to_camel


class SnakeToCamelAliases(BaseModel):
    class Config:
        allow_population_by_field_name = True
        alias_generator = snake_to_camel
