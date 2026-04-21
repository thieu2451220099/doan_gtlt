class Solution:
    def divide(self, dividend, divisor):
        # xử lý tràn
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # xác định dấu
        negative = (dividend < 0) ^ (divisor < 0)

        a = abs(dividend)
        b = abs(divisor)

        count = 0

        # trừ dần
        while a >= b:
            a -= b
            count += 1

        return -count if negative else count