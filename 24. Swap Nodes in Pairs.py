class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            a = prev.next
            b = a.next
            
            # swap
            prev.next = b
            a.next = b.next
            b.next = a
            
            # di chuyển prev
            prev = a
        
        return dummy.next