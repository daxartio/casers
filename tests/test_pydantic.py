from casers.pydantic import CamelAliases


def test_snake_to_camel_aliases():
    class Model(CamelAliases):
        snake_case: str

    assert Model(snake_case="value").snake_case == "value"
    assert Model(snakeCase="value").snake_case == "value"  # type: ignore
    assert Model.parse_obj({"snakeCase": "value"}).snake_case == "value"
