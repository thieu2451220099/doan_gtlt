class Solution:
    def minimumTotal(self, triangle):
        # bắt đầu từ hàng cuối
        dp = triangle[-1][:]

        # duyệt từ dưới lên
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]