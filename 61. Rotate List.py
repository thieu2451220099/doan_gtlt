class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # B1: tính độ dài
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        # B2: nối vòng
        tail.next = head

        # B3: giảm k
        k = k % n

        # B4: tìm điểm cắt
        steps = n - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next

        new_head = new_tail.next

        # B5: cắt vòng
        new_tail.next = None

        return new_head