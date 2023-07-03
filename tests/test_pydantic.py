import pytest
from packaging import version
from pydantic import __version__ as pydantic_version_raw

from casers.pydantic import CamelAliases

pydantic_version = version.parse(pydantic_version_raw)


@pytest.mark.skipif(
    pydantic_version >= version.parse("2.0.0"), reason="requires pydantic ^1"
)
def test_snake_to_camel_aliases_v1():
    class Model(CamelAliases):
        snake_case: str

    assert Model(snake_case="value").snake_case == "value"
    assert Model(snakeCase="value").snake_case == "value"  # type: ignore
    assert Model.parse_obj({"snakeCase": "value"}).snake_case == "value"


@pytest.mark.skipif(
    pydantic_version < version.parse("2.0.0"), reason="requires pydantic>=2.0.0"
)
def test_snake_to_camel_aliases_v2():
    class Model(CamelAliases):
        snake_case: str

    assert Model(snake_case="value").snake_case == "value"
    assert Model(snakeCase="value").snake_case == "value"  # type: ignore
    assert Model.model_validate({"snakeCase": "value"}).snake_case == "value"
