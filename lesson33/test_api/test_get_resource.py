import pytest
from unittest.mock import Mock
from unittest.mock import patch
from service import get_resource


@patch('service.requests.Session.get')
@pytest.mark.parametrize("res_id", [1, 100, 200])
# Positive tests
def test_get_resource_positive(mock_get, session, base_url, res_id):
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = {"id": res_id}
    response = get_resource(session, base_url, res_id)
    assert response.json()['id'] == res_id, "Wrong id"
    assert response.status_code == 200, "Status code is not 200"


@patch('service.requests.Session.get')
@pytest.mark.parametrize("res_id", [-1, 0, 201, "string", False, [1, 2, 3], None])
# Negative tests
def test_get_resource_negative(mock_get, session, base_url, res_id):
    mock_get.return_value = Mock(status_code=404)
    mock_get.return_value.json.return_value = []
    response = get_resource(session, base_url, res_id)
    assert len(response.json()) == 0, "Response is not empty"
    assert response.status_code == 404, "Status code is not 404"
