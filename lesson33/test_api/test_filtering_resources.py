import pytest
from unittest.mock import Mock
from unittest.mock import patch
from service import filter_resource_by_id, filter_resource_by_userid, \
    filter_resource_by_completed, filter_resource_by_title


@patch('service.requests.Session.get')
@pytest.mark.parametrize("res_id", [1, 100, 200])
# Positive tests
def test_filtering_positive_by_id(mock_get, session, base_url, res_id):
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = [{"id": res_id}]
    response = filter_resource_by_id(session, base_url, res_id)
    assert response.status_code == 200, "Status code is not 200"
    assert len(response.json()) == 1, "Length is more than 1"
    assert response.json()[0]["id"] == res_id, "Wrong id"


@patch('service.requests.Session.get')
@pytest.mark.parametrize("userid_positive", [1, 5, 10])
# Positive tests - search by userId
def test_filtering_positive_by_userid(mock_get, session, base_url, userid_positive):
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = [{"userId": userid_positive},
                                               {"userId": userid_positive},
                                               {"userId": userid_positive}]
    response = filter_resource_by_userid(session, base_url, userid_positive)
    assert response.status_code == 200, "Status code is not 200"
    todo = response.json()
    for i in todo:
        assert i["userId"] == userid_positive, "Wrong userId"


@patch('service.requests.Session.get')
@pytest.mark.parametrize("completed_positive", [True, False])
# Positive tests - search by completed
def test_filtering_positive_by_completed(mock_get, session, base_url, completed_positive):
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = [{"completed": completed_positive},
                                               {"completed": completed_positive},
                                               {"completed": completed_positive}]
    response = filter_resource_by_completed(session, base_url, completed_positive)
    assert response.status_code == 200, "Status code is not 200"
    todo = response.json()
    for i in todo:
        assert i["completed"] == completed_positive, "Wrong completed"


@patch('service.requests.Session.get')
@pytest.mark.parametrize("title_positive", [
    "et praesentium aliquam est",
    "fugiat aut voluptatibus corrupti deleniti velit iste odio",
    "voluptates dignissimos sed doloribus animi quaerat aut",
    "ipsam aperiam voluptates qui",
    "delectus aut autem"
])
# Positive tests - search by title
def test_filtering_positive_by_title(mock_get, session, base_url, title_positive):
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = [{"title": title_positive}]

    response = filter_resource_by_title(session, base_url, title_positive)
    assert response.status_code == 200, "Status code is not 200"
    assert len(response.json()) == 1, "Length is more than 1"
    assert response.json()[0]["title"] == title_positive, "Wrong title"


@patch('service.requests.Session.get')
@pytest.mark.parametrize("res_id", [-1, 0, 201, "string", False, [1, 2, 3], None])
# Negative tests - search by id
def test_filtering_negative_by_id(mock_get, session, base_url, res_id):
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = []
    response = filter_resource_by_id(session, base_url, res_id)
    assert response.status_code == 200, "Status code is not 200"
    assert len(response.json()) == 0, "Length is more than 0"


@patch('service.requests.Session.get')
# Negative tests - search by userId
def test_filtering_negative_by_userid(mock_get, session, base_url):
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = []
    response = filter_resource_by_userid(session, base_url, "0")
    assert response.status_code == 200, "Status code is not 200"
    assert len(response.json()) == 0, "Length is more than 0"


@patch('service.requests.Session.get')
# Negative tests - search by completed
def test_filtering_negative_by_completed(mock_get, session, base_url):
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = []
    response = filter_resource_by_completed(session, base_url, "123")
    assert response.status_code == 200, "Status code is not 200"
    assert len(response.json()) == 0, "Length is more than 0"


@patch('service.requests.Session.get')
# Negative tests - search by title
def test_filtering_negative_by_title(mock_get, session, base_url):
    mock_get.return_value = Mock(status_code=200)
    mock_get.return_value.json.return_value = []
    title = "some title 2"
    response = filter_resource_by_title(session, base_url, title)
    assert response.status_code == 200, "Status code is not 200"
    assert len(response.json()) == 0, "Length is more than 0"
