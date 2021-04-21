import pytest
import requests
import json


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://jsonplaceholder.typicode.com/todos",
        help="Enter url"
    )


@pytest.fixture(scope="module")
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope="module")
def session():
    return requests.Session()


class TestClassFunc:
    def read_from_json(self):
        with open("todos.json", "r") as f:
            reader = json.load(f)
        return reader


@pytest.fixture
def fixture_funcs():
    return TestClassFunc()
