class Solution(object):
    def reverseBits(self, n):
        result = 0
        
        for i in range(32):        # lặp 32 bit
            result = result << 1   # dịch trái result
            result |= (n & 1)      # lấy bit cuối của n
            n = n >> 1             # dịch phải n
        
        return result