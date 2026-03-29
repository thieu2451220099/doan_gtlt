class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        # 1. Tìm giữa
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. Đảo ngược nửa sau
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # 3. So sánh
        left = head
        right = prev
        
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True