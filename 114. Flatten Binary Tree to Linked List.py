# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root):
        if not root:
            return

        # làm phẳng cây trái và phải
        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        # đưa cây trái sang phải
        root.left = None
        root.right = left

        # tìm cuối danh sách bên phải
        curr = root
        while curr.right:
            curr = curr.right

        # nối phần phải cũ vào cuối
        curr.right = right