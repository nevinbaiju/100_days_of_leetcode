class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node=root):
            if node:
                dfs(node.left)
                dfs(node.right)
                temp = node.left
                node.left = node.right
                node.right = temp
        
        dfs(root)

        return root
