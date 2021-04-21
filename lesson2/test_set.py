import pytest


class TestSet:
    @pytest.mark.parametrize("el", [{"apple", "kiwi", 1, "banana"}, {1, 50, 40, 70}, {False, 1, "apple", -100, "cat", 65}])
    def test_check_value_in_set(self, el):
        assert 1 in el, "Value not in every set"

    def test_add_value_to_set(self, fixture_set):
        assert fixture_set.add_value_to_set({1, 4, 5, 7}, 2000) \
               == {1, 5, 4, 7, 2000}, "Value not added to set"

    def test_get_len_set(self, fixture_set):
        assert fixture_set.get_len_set({"apple", "banana", "cherry"}) == 3, "Length of set is not 3"

    def test_clear_set(self, fixture_set):
        empty_set = fixture_set.clear_set({1, 2, 3, 5})
        assert len(empty_set) == 0, "Set is not empty"

    def test_join_sets(self, fixture_set):
        assert fixture_set.join_sets({1, 3, 5}, {4, 1, 2}) == {1, 3, 5, 2, 4}, "Fail join sets"
