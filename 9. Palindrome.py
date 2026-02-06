# class Solution(object):
#     def isPalindrome(self, x):
#         # Số âm hoặc số kết thúc bằng 0 (trừ 0) thì không phải palindrome
#         if x < 0 or (x % 10 == 0 and x != 0):
#             return False

#         reversed_half = 0

#         # Đảo nửa sau của số
#         while x > reversed_half:
#             reversed_half = reversed_half * 10 + x % 10
#             x //= 10

#         # So sánh (chẵn hoặc lẻ chữ số)
#         return x == reversed_half or x == reversed_half // 10
print("Nhập số: ");      