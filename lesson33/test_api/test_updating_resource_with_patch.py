import pytest
from unittest.mock import Mock
from unittest.mock import patch
from service import patch_resource_positive, patch_resource_negative


@patch('service.requests.Session.patch')
@pytest.mark.parametrize("res_id", [1, 100, 200])
# Test for valid id of resources
def test_update_resource_with_patch_positive_id(mock_patch, session, base_url, res_id):
    payload = {"title": "some title"}
    mock_patch.return_value = Mock(status_code=200)
    mock_patch.return_value.json.return_value = {"title": "some title", "id": res_id}
    response = patch_resource_positive(session, base_url, res_id, payload)
    assert response.status_code == 200, "Status code is not 200"
    assert response.json()["id"] == res_id, "Id is different"
    assert response.json()["title"] == payload["title"], "Wrong title"


@patch('service.requests.Session.patch')
# Test for update all keys
def test_update_resource_with_patch_positive_all_values(mock_patch, session, base_url):
    payload = {"title": "NEW Title", "completed": True, "userId": 10}
    mock_patch.return_value = Mock(status_code=200)
    mock_patch.return_value.json.return_value = {"title": "NEW Title", "completed": True, "userId": 10, "id": 1}
    response = patch_resource_positive(session, base_url, "1", payload)
    assert response.status_code == 200, "Status code is not 200"
    assert response.json()["id"] == 1, "Id is not 1"
    assert response.json()["title"] == payload["title"], "Wrong title"
    assert response.json()["completed"] == payload["completed"], "Wrong completed status"
    assert response.json()["userId"] == payload["userId"], "Wrong userId"


@patch('service.requests.Session.patch')
# Test for update some keys
def test_update_resource_with_patch_positive_few_values(mock_patch, session, base_url, fixture_funcs):
    payload = {"title": "NEW Title"}
    mock_patch.return_value = Mock(status_code=200)
    mock_patch.return_value.json.return_value = {"title": "NEW Title", "completed": False, "userId": 1, "id": 1}
    get_all_data = fixture_funcs.read_from_json()
    todo_1 = get_all_data[0]
#   При удалении мока разкомментировать строки ниже. Выше get_all_data и todo_1 закомментировать. Удалить fixture_funcs.
#    get_all_data = session.get(url=base_url)
#    todo_1 = get_all_data.json()[0]
    response = patch_resource_positive(session, base_url, "1", payload)
    assert response.status_code == 200, "Status code is not 200"
    assert response.json()["id"] == 1, "Id is not 1"
    assert response.json()["title"] == payload["title"], "Wrong title"
    assert response.json()["completed"] == todo_1["completed"], "Wrong completed status"
    assert response.json()["userId"] == todo_1["userId"], "Wrong userId"


@patch('service.requests.Session.patch')
# Check that nothing change if empty dict was sent
def test_update_resource_with_patch_positive_no_values(mock_patch, session, base_url, fixture_funcs):
    payload = {}
    mock_patch.return_value = Mock(status_code=200)
    mock_patch.return_value.json.return_value = \
        {"title": "delectus aut autem", "completed": False, "userId": 1, "id": 1}
    get_all_data = fixture_funcs.read_from_json()
    todo_1 = get_all_data[0]
#   При удалении мока разкомментировать строки ниже. Выше get_all_data и todo_1 закомментировать. Удалить fixture_funcs.
#    get_all_data = session.get(url=base_url)
#    todo_1 = get_all_data.json()[0]
    response = patch_resource_positive(session, base_url, "1", payload)
    assert response.status_code == 200, "Status code is not 200"
    assert response.json()["id"] == 1, "Id is not 1"
    assert response.json()["title"] == todo_1["title"], "Wrong title"
    assert response.json()["completed"] == todo_1["completed"], "Wrong completed status"
    assert response.json()["userId"] == todo_1["userId"], "Wrong userId"


@patch('service.requests.Session.patch')
# Negative tests
def test_update_resource_with_patch_negative(mock_patch, session, base_url):
    payload = {"a": 100}
    headers = {"Content-type": "application/json"}
    mock_patch.return_value = Mock(status_code=500)
    response = patch_resource_negative(session, base_url, "1", payload, headers)
    assert response.status_code == 500, "Status code is not 500"
