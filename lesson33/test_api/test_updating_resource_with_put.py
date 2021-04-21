import pytest
from unittest.mock import Mock
from unittest.mock import patch
from service import put_resource


@patch('service.requests.Session.put')
@pytest.mark.parametrize("res_id", [1, 100, 200])
# Test for valid id of resources
def test_update_resource_with_put_positive_id(mock_put, session, base_url, res_id):
    payload = {"title": "some title", "completed": True, "userId": 1}
    mock_put.return_value = Mock(status_code=200)
    mock_put.return_value.json.return_value = {"title": "some title", "completed": True, "userId": 1, "id": res_id}
    response = put_resource(session, base_url, res_id, payload)
    assert response.status_code == 200, "Status code is not 200"
    assert response.json()["id"] == res_id, "Id is different"
    assert response.json()["userId"] == payload["userId"], "Wrong userId"
    assert response.json()["title"] == payload["title"], "Wrong title"
    assert response.json()["completed"] == payload["completed"], "Wrong completed status"


@patch('service.requests.Session.put')
@pytest.mark.parametrize("res_payload", [
    {"title": "A", "completed": True, "userId": 1, "id": 1},
    {"title": "long_title_long_title_long_title_long_title_long", "completed": False, "userId": 10, "id": 1},
    {"title": "Medium title", "completed": True, "userId": 10, "id": 1},
    {"title": " Title   with   wihtspaces ", "completed": False, "userId": 11, "id": 1},
    {"title": "Title with symbols *^[]/;< ", "completed": True, "userId": 5, "id": 1}
])
# Checking the replacement with valid data for resource 1
def test_update_resource_with_put_positive_body(mock_put, session, base_url, res_payload):
    mock_put.return_value = Mock(status_code=200)
    mock_put.return_value.json.return_value = res_payload
    response = put_resource(session, base_url, "1", res_payload)
    assert response.status_code == 200, "Status code is not 200"
    assert response.json()["id"] == 1, "Id is different"
    assert response.json()["userId"] == res_payload["userId"], "Wrong userId"
    assert response.json()["title"] == res_payload["title"], "Wrong title"
    assert response.json()["completed"] == res_payload["completed"], "Wrong completed"


@patch('service.requests.Session.put')
# Checking the replacement of resource 1 with an empty payload
def test_update_resource_with_put_positive_empty_body(mock_put, session, base_url):
    payload = {}
    mock_put.return_value = Mock(status_code=200)
    mock_put.return_value.json.return_value = {"id": 1}
    response = put_resource(session, base_url, "1", payload)
    assert response.status_code == 200, "Status code is not 200"
    assert len(response.json()) == 1, "Length is not 1"
    assert response.json()["id"] == 1, "Wrong id"
    assert "userId" not in response.json(), "userId in dict"
    assert "title" not in response.json(), "title in dict"
    assert "completed" not in response.json(), "completed in dict"


@patch('service.requests.Session.put')
# Checking the replacement of resource 1 with an empty payload with a part of the data
def test_update_resource_with_put_positive_body_without_title(mock_put, session, base_url):
    payload = {"completed": True, "userId": 1}
    mock_put.return_value = Mock(status_code=200)
    mock_put.return_value.json.return_value = {"completed": True, "userId": 1, "id": 1}
    response = put_resource(session, base_url, "1", payload)
    assert response.status_code == 200, "Status code is not 200"
    assert len(response.json()) == 3, "Length is not 3"
    assert response.json()["id"] == 1, "Wrong id"
    assert response.json()["completed"] == payload["completed"], "Wrong completed status"
    assert response.json()["userId"] == payload["userId"], "Wrong userId"
    assert "title" not in response.json(), "title in dict"
    print(response.json())


@patch('service.requests.Session.put')
@pytest.mark.parametrize("res_id", [-1, 0, 201, "string", False, [1, 2, 3], None])
# Negative tests - checking for invalid id
def test_update_resource_with_put_negative_id(mock_put, session, base_url, res_id):
    payload = {"title": "some title", "completed": True, "userId": 1}
    mock_put.return_value = Mock(status_code=500)
    response = put_resource(session, base_url, res_id, payload)
    assert response.status_code == 500, "Status code is not 500"
