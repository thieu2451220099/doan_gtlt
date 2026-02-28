class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy
        
        # fast đi trước n+1 bước
        for _ in range(n + 1):
            fast = fast.next
        
        # chạy cùng lúc
        while fast:
            fast = fast.next
            slow = slow.next
        
        # xóa node thứ n từ cuối
        slow.next = slow.next.next
        
        return dummy.next