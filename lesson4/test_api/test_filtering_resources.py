# Positive tests - search by id
def test_filtering_positive_by_id(session, base_url, fixture_id_positive):
    res = session.get(url=f'{base_url}?id={fixture_id_positive}')
    assert res.status_code == 200, "Status code is not 200"
    assert len(res.json()) == 1, "Length is more than 1"
    assert res.json()[0]["id"] == fixture_id_positive, "Wrong id"


# Positive tests - search by userId
def test_filtering_positive_by_userid(session, base_url, fixture_userid_positive):
    res = session.get(url=f'{base_url}?userId={fixture_userid_positive}')
    assert res.status_code == 200, "Status code is not 200"
    todo = res.json()
    for i in todo:
        assert i["userId"] == fixture_userid_positive, "Wrong userId"


# Positive tests - search by completed
def test_filtering_positive_by_completed(session, base_url, fixture_completed_positive):
    res = session.get(url=f'{base_url}?completed={fixture_completed_positive}')
    assert res.status_code == 200, "Status code is not 200"
    todo = res.json()
    for i in todo:
        assert i["completed"] == fixture_completed_positive, "Wrong completed"


# Positive tests - search by title
def test_filtering_positive_by_title(session, base_url, fixture_title_positive):
    res = session.get(url=f'{base_url}?title={fixture_title_positive}')
    assert res.status_code == 200, "Status code is not 200"
    assert len(res.json()) == 1, "Length is more than 1"
    assert res.json()[0]["title"] == fixture_title_positive, "Wrong title"


# Negative tests - search by id
def test_filtering_negative_by_id(session, base_url, fixture_id_negative):
    res = session.get(url=f'{base_url}?id={fixture_id_negative}')
    assert res.status_code == 200, "Status code is not 200"
    assert len(res.json()) == 0, "Length is more than 0"


# Negative tests - search by userId
def test_filtering_negative_by_userid(session, base_url):
    res = session.get(url=f'{base_url}?userId=0')
    assert res.status_code == 200, "Status code is not 200"
    assert len(res.json()) == 0, "Length is more than 0"


# Negative tests - search by completed
def test_filtering_negative_by_completed(session, base_url):
    res = session.get(url=f'{base_url}?completed=123')
    assert res.status_code == 200, "Status code is not 200"
    assert len(res.json()) == 0, "Length is more than 0"


# Negative tests - search by title
def test_filtering_negative_by_title(session, base_url):
    title = "some title 2"
    res = session.get(url=f'{base_url}?title={title}')
    assert res.status_code == 200, "Status code is not 200"
    assert len(res.json()) == 0, "Length is more than 0"
