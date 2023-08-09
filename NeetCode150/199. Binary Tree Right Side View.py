# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []

        def dfs(node=root, level=0):
            if not node:
                return
            if len(ans) < level+1:
                ans.append(node.val)
            dfs(node.right, level+1)
            dfs(node.left, level+1)

        dfs()
        
        return ans
