# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(node=root):
            nonlocal res
            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                res = max(res, left+right)

                return 1 + max(left, right)
            else:
                return 0

        dfs()

        return res

