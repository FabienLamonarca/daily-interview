from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        counter = 1

        for layer in range(0, int((n + 1) / 2), 1):
            # direction 1 - traverse from left to right
            for ptr in range(layer, n - layer, 1):
                matrix[layer][ptr] = counter
                counter = counter + 1

            # direction 2 - traverse from top to bottom
            for ptr in range(layer + 1, n - layer):
                matrix[ptr][n - layer - 1] = counter
                counter = counter + 1

            # direction 3 - traverse from right to left
            for ptr in range(layer + 1, n - layer, 1):
                matrix[n - layer - 1][n - ptr - 1] = counter
                counter = counter + 1

            # direction 4 - traverse from bottom to top
            for ptr in range(layer + 1, n - layer - 1, 1):
                matrix[n - ptr - 1][layer] = counter
                counter = counter + 1

        return matrix
