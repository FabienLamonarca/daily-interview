from unittest import TestCase

from leetcode.spiral_matrix_II import Solution


class TestSolution(TestCase):
    solution = Solution()

    def test_generate_matrix(self):
        assert self.solution.generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
