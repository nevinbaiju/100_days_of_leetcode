# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = root.val

        def dfs(node=root):
            nonlocal res

            if node:
                left = max(0, dfs(node.left))
                right = max(0, dfs(node.right))
                curr_res = node.val + left + right
                res = max(res, curr_res)
                return max(node.val + left, node.val + right)
            else:
                return 0

        dfs(root)

        return res
