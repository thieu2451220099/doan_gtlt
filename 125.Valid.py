class Solution(object):
    def isPalindrome(self, s):
        filtered = []
        for ch in s:
            if ch.isalnum():          # chỉ lấy chữ và số
                filtered.append(ch.lower())

        return filtered == filtered[::-1]
