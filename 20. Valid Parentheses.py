class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for ch in s:
            # Nếu là ngoặc mở thì đẩy vào stack
            if ch in pairs.values():
                stack.append(ch)
            else:
                # Nếu gặp ngoặc đóng mà stack rỗng → sai
                if not stack:
                    return False

                # Lấy ngoặc mở gần nhất
                top = stack.pop()

                # Kiểm tra có khớp không
                if pairs[ch] != top:
                    return False

        # Sau khi duyệt xong, stack phải rỗng
        return len(stack) == 0

        