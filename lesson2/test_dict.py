class TestDict:
    def test_get_value(self, fixture_dict):
        assert fixture_dict.get_value({"a": 10, "b": 20, "c": 30}, "b") == 20, "Wrong value for key"

    def test_add_key_to_dict(self, fixture_dict):
        d = fixture_dict.add_key_to_dict({"a": 10, "b": 20, "c": 30}, "d", 40)
        assert d.get("d") == 40, "No such key"

    def test_del_key_from_dict(self, fixture_dict):
        d = fixture_dict.del_key_from_dict({"a": 123, "bb": 10, "c": 90, "d": 0}, "bb")
        assert "bb" not in d, "Value in dictionary"

    def test_copy_dict(self, fixture_dict):
        assert fixture_dict.copy_dict({"a": 10, "b": 20, "c": 30}) == \
               {"a": 10, "b": 20, "c": 30}, "Copy is not created"

    def test_get_len_dicts(self, fixture_get_len_dicts):
        assert len(fixture_get_len_dicts) == 2, "Length of dicts is not 2"
