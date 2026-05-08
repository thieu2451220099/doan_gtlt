class Solution:
    def maxProfit(self, prices):
        profit = 0

        for i in range(1, len(prices)):
            # nếu giá hôm nay lớn hơn hôm qua thì cộng lợi nhuận
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit