class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root: return []
        res, q, r = [], [root], 0
        while q:
            level = [n.val for n in q]
            if r: level.reverse()
            res.append(level)
            q = [c for n in q for c in (n.left,n.right) if c]
            r ^= 1
        return res