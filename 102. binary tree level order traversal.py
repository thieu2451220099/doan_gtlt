class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        res, q = [], [root]

        while q:
            res.append([node.val for node in q])
            q = [child for node in q for child in (node.left, node.right) if child]

        return res