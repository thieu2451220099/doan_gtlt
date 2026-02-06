class Solution(object):
    def strStr(self, haystack, needle):
        # Nếu needle dài hơn haystack thì không thể tìm
        if len(needle) > len(haystack):
            return -1

        # Duyệt từng vị trí có thể bắt đầu
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1
