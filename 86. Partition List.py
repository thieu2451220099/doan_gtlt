class Solution(object):
    def partition(self, head, x):
        small = ListNode()
        big = ListNode()
        s, b = small, big

        while head:
            if head.val < x:
                s.next = head
                s = s.next
            else:
                b.next = head
                b = b.next
            head = head.next

        s.next = big.next
        b.next = None
        return small.next