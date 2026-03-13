class Solution(object):
    def generateTrees(self, n):
        def dfs(l, r):
            if l > r:
                return [None]
            
            res = []
            for i in range(l, r+1):
                for left in dfs(l, i-1):
                    for right in dfs(i+1, r):
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res
        
        return dfs(1, n)
        