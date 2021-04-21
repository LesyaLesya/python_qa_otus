import pytest
from unittest.mock import Mock
from unittest.mock import patch
from service import post_resource_positive, post_resource_negative


@patch('service.requests.Session.post')
@pytest.mark.parametrize("res_payload", [
    {"title": "A", "completed": True, "userId": 1, "id": 201},
    {"title": "long_title_long_title_long_title_long_title_long", "completed": False, "userId": 10, "id": 201},
    {"title": "Medium title", "completed": True, "userId": 10, "id": 201},
    {"title": " Title   with   wihtspaces ", "completed": False, "userId": 11, "id": 201},
    {"title": "Title with symbols *^[]/;< ", "completed": True, "userId": 5, "id": 201}
])
# Positive tests
def test_post_resource_positive(mock_post, session, base_url, res_payload):
    mock_post.return_value = Mock(status_code=201)
    mock_post.return_value.json.return_value = res_payload
    response = post_resource_positive(session, base_url, res_payload)
    assert response.status_code == 201, "Status code is not 201"
    assert response.json()["id"] == 201, "ID of post is not 201"
    assert response.json()["userId"] == res_payload["userId"], "Wrong userId"
    assert response.json()["title"] == res_payload["title"], "Wrong title"
    assert response.json()["completed"] == res_payload["completed"], "Wrong completed"


@patch('service.requests.Session.post')
# Negative tests
def test_post_resource_negative(mock_post, session, base_url):
    payload = {"a": 100}
    headers = {"Content-type": "application/json"}
    mock_post.return_value = Mock(status_code=500)
    response = post_resource_negative(session, base_url, payload, headers)
    assert response.status_code == 500, "Status code is not 500"
