class Solution:
    def reverseKGroup(self, head, k):
        def reverse(start, end):
            prev = end
            while start != end:
                nxt = start.next
                start.next = prev
                prev = start
                start = nxt
            return prev

        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while True:
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next
            start = groupPrev.next

            # đảo đoạn k node
            groupPrev.next = reverse(start, groupNext)

            # cập nhật lại vị trí
            groupPrev = start