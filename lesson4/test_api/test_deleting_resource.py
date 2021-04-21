# Positive tests
def test_deleting_resource_positive(session, base_url, fixture_id_positive):
    res = session.delete(url=f'{base_url}/{fixture_id_positive}')
    assert res.status_code == 200, "Status code is not 200"
    assert not res.json()


# Negative tests - нельзя вызвать ошибку 4хх или 5хх, всегда возращается 200 и пустой словарь
# def test_deleting_resource_negative(session, base_url, fixture_id_negative):
#     res = session.delete(url=f'{base_url}/{fixture_id_negative}')
#     assert res.status_code == 404, "status code is not 404"
#     print(res.json())
