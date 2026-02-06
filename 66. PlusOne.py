class Solution(object):
    def plusOne(self, digits):
        # Duyệt từ chữ số cuối cùng
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        # Nếu tất cả đều là 9 (ví dụ: [9], [9,9])
        return [1] + digits
