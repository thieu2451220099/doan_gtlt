class Solution:
    def maxProfit(self, prices):
        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            # cập nhật giá nhỏ nhất
            minPrice = min(minPrice, price)

            # cập nhật lợi nhuận lớn nhất
            maxProfit = max(maxProfit, price - minPrice)

        return maxProfit