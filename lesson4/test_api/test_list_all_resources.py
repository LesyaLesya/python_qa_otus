import pytest


def test_get_all_resources(session, base_url):
    res = session.get(url=base_url)
    assert res.status_code == 200, "Status code is not 200"
    assert len(res.json()) == 200, "List no 200 entities"


@pytest.mark.parametrize("id, user_id, title, completed", [
    (1, 1, "delectus aut autem", False),
    (200, 10, "ipsam aperiam voluptates qui", False),
])
def test_get_all_resources_last_first(id, session, base_url,  user_id, title, completed):
    res = session.get(url=base_url)
    idx = id - 1
    assert res.json()[idx]["id"] == id, f"El's id is not {id}"
    assert res.json()[idx]["userId"] == user_id, "Wrong userId"
    assert res.json()[idx]["title"] == title, "Wrong title"
    assert res.json()[idx]["completed"] is completed, "Wrong completed status"
