# Test for valid id of resources
def test_update_resource_with_put_positive_id(session, base_url, fixture_id_positive):
    payload = {"title": "some title", "completed": True, "userId": 1}
    res = session.put(url=f'{base_url}/{fixture_id_positive}', json=payload)
    assert res.status_code == 200, "Status code is not 200"
    assert res.json()["id"] == fixture_id_positive, "Id is different"
    assert res.json()["userId"] == payload["userId"], "Wrong userId"
    assert res.json()["title"] == payload["title"], "Wrong title"
    assert res.json()["completed"] == payload["completed"], "Wrong completed status"


# Checking the replacement with valid data for resource 1
def test_update_resource_with_put_positive_body(session, base_url, fixture_payload_positive):
    res = session.put(url=f'{base_url}/1', json=fixture_payload_positive)
    assert res.status_code == 200, "Status code is not 200"
    assert res.json()["id"] == 1, "Id is different"
    assert res.json()["userId"] == fixture_payload_positive["userId"], "Wrong userId"
    assert res.json()["title"] == fixture_payload_positive["title"], "Wrong title"
    assert res.json()["completed"] == fixture_payload_positive["completed"], "Wrong completed"


# Checking the replacement of resource 1 with an empty payload
def test_update_resource_with_put_positive_empty_body(session, base_url):
    payload = {}
    res = session.put(url=f'{base_url}/1', json=payload)
    assert res.status_code == 200, "Status code is not 200"
    assert len(res.json()) == 1, "Length is not 1"
    assert res.json()["id"] == 1, "Wrong id"
    assert "userId" not in res.json(), "userId in dict"
    assert "title" not in res.json(), "title in dict"
    assert "completed" not in res.json(), "completed in dict"


# Checking the replacement of resource 1 with an empty payload with a part of the data
def test_update_resource_with_put_positive_body_without_title(session, base_url):
    payload = {"completed": True, "userId": 1}
    res = session.put(url=f'{base_url}/1', json=payload)
    assert res.status_code == 200, "Status code is not 200"
    assert len(res.json()) == 3, "Length is not 3"
    assert res.json()["id"] == 1, "Wrong id"
    assert res.json()["completed"] == payload["completed"], "Wrong completed status"
    assert res.json()["userId"] == payload["userId"], "Wrong userId"
    assert "title" not in res.json(), "title in dict"


# Negative tests - checking for invalid id
def test_update_resource_with_put_negative_id(session, base_url, fixture_id_negative):
    payload = {"title": "some title", "completed": True, "userId": 1}
    res = session.put(url=f'{base_url}/{fixture_id_negative}', json=payload)
    assert res.status_code == 500, "Status code is not 500"
