class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # 1. transpose (đổi hàng ↔ cột)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2. reverse từng hàng
        for row in matrix:
            row.reverse()