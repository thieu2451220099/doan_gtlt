# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        # tìm điểm gặp nhau
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        # tìm node bắt đầu cycle
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow