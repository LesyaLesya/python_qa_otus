import json
from jsonschema import validate


def validate_schema(data, schema_file):
    with open(schema_file) as file:
        schema = json.load(file)
    return validate(instance=data, schema=schema)


def test_get_todos(session, base_url, fixture_get_todos):
    res = session.get(url=base_url)
    validate_schema(res.json(), fixture_get_todos)


def test_get_todo(session, base_url):
    res = session.get(url=f'{base_url}/1')
    validate_schema(res.json(), "lesson4/schemas/todo_schema.json")
