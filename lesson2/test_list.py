import pytest


class TestList:
    def test_get_len_list(self, fixture_list):
        assert fixture_list.get_len_list([1, 3, "abc", True, 0, "test"]) == 6, "Wrong length for list"

    @pytest.mark.parametrize("el", [[1, 2, 5, 6, 10, 100], [1, -1, 73, 65], [1, "test", 4, 90], [1, True, 87, -65]])
    def test_first_list_el_is_one(self, el):
        assert el[0] == 1, "First el in list is not One"

    def test_change_first_el_in_lst(self, fixture_list):
        assert fixture_list.change_first_el_in_lst([1, 2, 3, 4, 5], "cat")[0] \
               == "cat", "First element is not 'cat'"

    def test_append_value_to_list(self, fixture_list):
        assert fixture_list.append_value_to_list([1, 7, 10, 12], 1000) \
               == [1, 7, 10, 12, 1000], "Not success appending to list"

    def test_concat_lists(self, fixture_list):
        assert fixture_list.concat_lists([1, 2, 3], [4, 5, 6]) \
               == [1, 2, 3, 4, 5, 6], "Fail concatenating or wrong order of els"
