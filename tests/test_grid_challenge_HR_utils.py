from main_code.grid_challenge_HR import gridChallenge
import unittest

class GridChallengeTest(unittest.TestCase):

    def test_give_abc_def_ghi(self):
        grid = ["abc", "def", "ghi"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")

    def test_give_sorted_rows_after_sorting(self):
        grid = ["cba", "fed", "ihg"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")

    def test_give_unsorted_column(self):
        grid = ["abc", "def", "ihg"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")

    def test_single_row(self):
        grid = ["abc"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")

    def test_unsorted_rows(self):
        grid = ["dcba", "zyxw", "tsrq"]
        result = gridChallenge(grid)
        self.assertEqual(result, "NO")

    def test_unsorted_column_after_sorting(self):
        grid = ["abc", "cde", "ghi"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")

    def test_all_rows_identical(self):
        grid = ["aaa", "aaa", "aaa"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")

    def test_rows_and_columns_sorted(self):
        grid = ["abc", "fgh", "ijk"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")

    def test_mixed_characters(self):
        grid = ["abc", "wxyz", "def"]
        result = gridChallenge(grid)
        self.assertEqual(result, "NO")

    def test_large_grid_with_unsorted_column(self):
        grid = ["zyxw", "abcd", "wxyz", "ghij"]
        result = gridChallenge(grid)
        self.assertEqual(result, "NO")

