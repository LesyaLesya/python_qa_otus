import pytest
import requests


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


@pytest.fixture(params=[1, 100, 200])
def fixture_id_positive(request):
    return request.param


@pytest.fixture(params=[-1, 0, 201, "string", False, [1, 2, 3], None])
def fixture_id_negative(request):
    return request.param


@pytest.fixture(params=[{"title": "A", "completed": True, "userId": 1},
                        {"title": "long_title_long_title_long_title_long_title_long", "completed": False, "userId": 10},
                        {"title": "Medium title", "completed": True, "userId": 10},
                        {"title": " Title   with   wihtspaces ", "completed": False, "userId": 11},
                        {"title": "Title with symbols *^[]/;< ", "completed": True, "userId": 5}])
def fixture_payload_positive(request):
    return request.param


@pytest.fixture(params=[1, 5, 10])
def fixture_userid_positive(request):
    return request.param


@pytest.fixture(params=[True, False])
def fixture_completed_positive(request):
    return request.param


@pytest.fixture(params=["et praesentium aliquam est",
                        "fugiat aut voluptatibus corrupti deleniti velit iste odio",
                        "voluptates dignissimos sed doloribus animi quaerat aut",
                        "ipsam aperiam voluptates qui",
                        "delectus aut autem"])
def fixture_title_positive(request):
    return request.param


@pytest.fixture(params=["lesson4/schemas/todos_schema.json",
                        "lesson4/schemas/todos_schema_file.json"])
def fixture_get_todos(request):
    return request.param
