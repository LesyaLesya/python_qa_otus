import pytest
from unittest.mock import Mock
from unittest.mock import patch
from service import delete_resource


@patch('service.requests.Session.delete')
@pytest.mark.parametrize("res_id", [1, 100, 200])
# Positive tests
def test_deleting_resource_positive(mock_del, session, base_url, res_id):
    mock_del.return_value = Mock(status_code=200)
    mock_del.return_value.json.return_value = None
    response = delete_resource(session, base_url, res_id)
    assert response.status_code == 200, "Status code is not 200"
    assert not response.json()


# Negative tests - нельзя вызвать ошибку 4хх или 5хх, всегда возращается 200 и пустой словарь
# def test_deleting_resource_negative(session, base_url, fixture_id_negative):
#     res = session.delete(url=f'{base_url}/{fixture_id_negative}')
#     assert res.status_code == 404, "status code is not 404"
#     print(res.json())
