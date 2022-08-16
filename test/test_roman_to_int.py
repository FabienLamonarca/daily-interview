from unittest import TestCase

from leetcode.roman_to_int import Solution


class TestSolution(TestCase):
    solution = Solution()

    def test_roman_to_int_1(self):
        assert self.solution.roman_to_int("III") == 3

    def test_roman_to_int_2(self):
        assert self.solution.roman_to_int("LVIII") == 58

    def test_roman_to_int_3(self):
        assert self.solution.roman_to_int("MCMXCIV") == 1994
