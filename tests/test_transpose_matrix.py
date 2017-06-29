import unittest
from transpose_matrix import transpose_matrix


class TestTransposeMatrix(unittest.TestCase):
    def test1(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        self.assertEquals([[1, 4], [2, 5], [3, 6]], transpose_matrix(matrix, 2, 3))

    def test2(self):
        matrix = [[1]]
        self.assertEquals([[1]], transpose_matrix(matrix, 1, 1))

    def test3(self):
        matrix = []
        self.assertEquals([], transpose_matrix(matrix, 0, 0))

    def test4(self):
        matrix = [[1, 2, 3, 4]]
        self.assertEquals([[1], [2], [3], [4]], transpose_matrix(matrix, 1, 4))

    def test5(self):
        matrix = [[1, 2], [3, 4]]
        self.assertEquals([[1, 3], [2, 4]], transpose_matrix(matrix, 2, 2))
