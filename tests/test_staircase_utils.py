from main_code.staircase import staircase
import unittest

import unittest

class TestStaircase(unittest.TestCase):

    def test_give_2_with_hash_should_be_hh(self):
        n = 2
        pattern = '#'
        expected_output = " #\n##\n"

        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_3_with_star_should_be_star_staircase(self):
        n = 3
        pattern = '*'
        expected_output = "  *\n **\n***\n"

        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_1_with_hash_should_be_single_hash(self):
        n = 1
        pattern = '#'
        expected_output = "#\n"

        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_4_with_dollar_should_be_dollar_staircase(self):
        n = 4
        pattern = '$'
        expected_output = "   $\n  $$\n $$$\n$$$$\n"

        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_5_with_at_should_be_at_staircase(self):
        n = 5
        pattern = '@'
        expected_output = "    @\n   @@\n  @@@\n @@@@\n@@@@@\n"

        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_0_with_hash_should_be_empty_string(self):
        n = 0
        pattern = '#'
        expected_output = ""

        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_10_with_x_should_be_x_staircase(self):
        n = 10
        pattern = 'x'
        expected_output = (
            "         x\n"
            "        xx\n"
            "       xxx\n"
            "      xxxx\n"
            "     xxxxx\n"
            "    xxxxxx\n"
            "   xxxxxxx\n"
            "  xxxxxxxx\n"
            " xxxxxxxxx\n"
            "xxxxxxxxxx\n"
        )

        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_2_with_empty_pattern_should_be_empty_staircase(self):
        n = 2
        pattern = ''
        expected_output = " \n\n"
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_3_with_multiple_char_pattern_should_be_staircase(self): 
        n = 3
        pattern = 'abc'
        expected_output = "  abc\n abcabc\nabcabcabc\n"

        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_4_with_special_char_pattern_should_be_staircase(self):
        n = 4
        pattern = '!@#'
        expected_output = "   !@#\n  !@#!@#\n !@#!@#!@#\n!@#!@#!@#!@#\n"

        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)