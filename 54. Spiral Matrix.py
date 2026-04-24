class Solution:
    def spiralOrder(self, matrix):
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # trái → phải
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            # trên → dưới
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                # phải → trái
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                # dưới → trên
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res