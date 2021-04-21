class TestString:
    def test_get_len_string(self, fixture_get_len_string):
        assert len(fixture_get_len_string) == 3, "Wrong length for string"
        print(f"Word '{fixture_get_len_string}' has length 3")

    def test_first_symbol_of_string(self, fixture_string):
        assert fixture_string.first_symbol_of_string("python") == "p", "Wrong first letter in word"

    def test_upper_word(self, fixture_string):
        assert fixture_string.upper_word("python") == "PYTHON", "Word not in upper case"

    def test_check_letter_in_sring(self, fixture_string):
        assert fixture_string.check_letter_in_string("o", "python"), "No such a letter in word"

    def test_replace_letter(self, fixture_string):
        assert fixture_string.replace_letter("d", "m", "day") == "may", "Wrong word after replace letters"

    def test_find_letter_index(self, fixture_string):
        assert fixture_string.find_letter_index("testing", "s") == 2, "Wrong index for letter position"

    def test_count_letter(self, fixture_string):
        assert fixture_string.count_letter("abbbbaaaua", "a") == 5, "Wrong count of letter"
