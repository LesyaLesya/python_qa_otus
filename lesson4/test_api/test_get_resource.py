# Positive tests
def test_get_resource_positive(session, base_url, fixture_id_positive):
    res = session.get(url=f'{base_url}/{fixture_id_positive}')
    assert res.status_code == 200, "Status code is not 200"
    assert res.json()["id"] == fixture_id_positive, "Id is different"


# Negative tests
def test_get_resource_negative(session, base_url, fixture_id_negative):
    res = session.get(url=f'{base_url}/{fixture_id_negative}')
    assert res.status_code == 404, "Status code is not 404"
    assert len(res.json()) == 0, "Dictionary is not empty"
