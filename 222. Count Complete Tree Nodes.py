class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        
        def getLeftHeight(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        def getRightHeight(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height
        
        left_height = getLeftHeight(root)
        right_height = getRightHeight(root)
        
        # Nếu là perfect binary tree
        if left_height == right_height:
            return (1 << left_height) - 1
        
        # Không phải → đệ quy
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        