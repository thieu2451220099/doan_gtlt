class Solution:
    def generate(self, numRows):
        result = []

        for i in range(numRows):
            row = [1] * (i + 1)

            # tính các phần tử ở giữa
            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]

            result.append(row)

        return result