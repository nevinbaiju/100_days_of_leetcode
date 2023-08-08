# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(node=root):
            nonlocal res

            if node:
                left = dfs(node.left)
                right = dfs(node.right)
                if abs(left - right) > 1:
                    res = False
                return 1 + max(left, right)

            else:
                return 0
        dfs()
        return res
