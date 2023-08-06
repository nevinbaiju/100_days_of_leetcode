class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, height=0):
            if not node:
                return height
            else:
                h1 = dfs(node.left, height+1)
                h2 = dfs(node.right, height+1)
                return max(h1, h2)
        
        return dfs(root)
