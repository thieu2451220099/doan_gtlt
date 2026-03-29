class Solution:
    def binaryTreePaths(self, root):
        result = []
        
        def dfs(node, path):
            if not node:
                return
            
            # Nếu là leaf
            if not node.left and not node.right:
                result.append(path + str(node.val))
                return
            
            # Đi tiếp
            dfs(node.left, path + str(node.val) + "->")
            dfs(node.right, path + str(node.val) + "->")
        
        dfs(root, "")
        return result