class Solution(object):
    def myAtoi(self, s):
        s = s.lstrip()  # bỏ khoảng trắng đầu
        
        if not s:
            return 0
        
        sign = 1
        index = 0
        result = 0
        
        # kiểm tra dấu
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1
        
        # đọc các chữ số
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            result = result * 10 + digit
            index += 1
        
        result *= sign
        
        # giới hạn 32-bit
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result
