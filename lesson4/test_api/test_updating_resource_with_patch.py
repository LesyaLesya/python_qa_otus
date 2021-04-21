# Test for valid id of resources
def test_update_resource_with_patch_positive_id(session, base_url, fixture_id_positive):
    payload = {"title": "some title"}
    res = session.patch(url=f'{base_url}/{fixture_id_positive}', json=payload)
    assert res.status_code == 200, "Status code is not 200"
    assert res.json()["id"] == fixture_id_positive, "Id is different"
    assert res.json()["title"] == payload["title"], "Wrong title"


# Test for update all keys
def test_update_resource_with_patch_positive_all_values(session, base_url):
    payload = {"title": "NEW Title", "completed": True, "userId": 10}
    res = session.patch(url=f'{base_url}/1', json=payload)
    assert res.status_code == 200, "Status code is not 200"
    assert res.json()["id"] == 1, "Id is not 1"
    assert res.json()["title"] == payload["title"], "Wrong title"
    assert res.json()["completed"] == payload["completed"], "Wrong completed status"
    assert res.json()["userId"] == payload["userId"], "Wrong userId"


# Test for update some keys
def test_update_resource_with_patch_positive_few_values(session, base_url):
    get_all_data = session.get(url=base_url)
    todo_1 = get_all_data.json()[0]
    payload = {"title": "NEW Title"}
    res = session.patch(url=f'{base_url}/1', json=payload)
    assert res.status_code == 200, "Status code is not 200"
    assert res.json()["id"] == 1, "Id is not 1"
    assert res.json()["title"] == payload["title"], "Wrong title"
    assert res.json()["completed"] == todo_1["completed"], "Wrong completed status"
    assert res.json()["userId"] == todo_1["userId"], "Wrong userId"


# Check that nothing change if empty dict was sent
def test_update_resource_with_patch_positive_no_values(session, base_url):
    get_all_data = session.get(url=base_url)
    todo_1 = get_all_data.json()[0]
    payload = {}
    res = session.patch(url=f'{base_url}/1', json=payload)
    assert res.status_code == 200, "Status code is not 200"
    assert res.json()["id"] == 1, "Id is not 1"
    assert res.json()["title"] == todo_1["title"], "Wrong title"
    assert res.json()["completed"] == todo_1["completed"], "Wrong completed status"
    assert res.json()["userId"] == todo_1["userId"], "Wrong userId"


# Negative tests
def test_update_resource_with_patch_negative(session, base_url):
    payload = {"a": 100}
    res = session.patch(url=f'{base_url}/1',
                        data=payload, headers={"Content-type": "application/json"})
    assert res.status_code == 500, "Status code is not 500"
