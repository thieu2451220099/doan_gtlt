class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        res = ""

        # hàm mở rộng từ tâm
        def expand(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(n):
            # palindrome lẻ
            p1 = expand(i, i)
            # palindrome chẵn
            p2 = expand(i, i + 1)

            if len(p1) > len(res):
                res = p1
            if len(p2) > len(res):
                res = p2

        return res
