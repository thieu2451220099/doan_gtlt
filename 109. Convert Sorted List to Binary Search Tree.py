class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None

        # chỉ có 1 node
        if not head.next:
            return TreeNode(head.val)

        # tìm node giữa
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # cắt list bên trái
        prev.next = None

        # node giữa làm root
        root = TreeNode(slow.val)

        # tạo cây con trái và phải
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root