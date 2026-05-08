class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        # nếu không có cây con trái
        if not root.left:
            return self.minDepth(root.right) + 1

        # nếu không có cây con phải
        if not root.right:
            return self.minDepth(root.left) + 1

        # có cả 2 cây con
        return min(self.minDepth(root.left),
                   self.minDepth(root.right)) + 1