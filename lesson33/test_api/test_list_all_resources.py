import pytest
from unittest.mock import Mock
from unittest.mock import patch
from service import get_all_resources


@patch('service.requests.Session.get')
def test_get_all_resources(mock_get, session, base_url, fixture_funcs):
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = fixture_funcs.read_from_json()
    response = get_all_resources(session, base_url)
    assert response.status_code == 200, "Status code is not 200"
    assert len(response.json()) == 200, "List no 200 entities"


@patch('service.requests.Session.get')
@pytest.mark.parametrize("id, user_id, title, completed", [
    (1, 1, "delectus aut autem", False),
    (200, 10, "ipsam aperiam voluptates qui", False)])
def test_get_all_resources_last_first(mock_get, session, base_url, fixture_funcs, id, user_id, title, completed):
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = fixture_funcs.read_from_json()
    idx = id - 1
    response = get_all_resources(session, base_url)
    assert response.json()[idx]["id"] == id, f"El's id is not {id}"
    assert response.json()[idx]["userId"] == user_id, "Wrong userId"
    assert response.json()[idx]["title"] == title, "Wrong title"
    assert response.json()[idx]["completed"] is completed, "Wrong completed status"
