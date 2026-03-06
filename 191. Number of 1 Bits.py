class Solution(object):
    def hammingWeight(self, n):
        count = 0
        
        while n > 0:
            count += n & 1   # nếu bit cuối là 1 thì cộng
            n = n >> 1       # dịch phải
        
        return count