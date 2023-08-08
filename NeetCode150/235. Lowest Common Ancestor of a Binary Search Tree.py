# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def findPath(self, root, key):
        res = [root]

        while root != key:
            if key.val > root.val:
                root = root.right
            else:
                root = root.left
            res.append(root)
        
        return res
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p = self.findPath(root, p)
        path_q = self.findPath(root, q)

        ans = None

        while path_p and path_q and path_p[0] == path_q[0]:
            ans = path_p[0]
            
            path_p.pop(0)
            path_q.pop(0)
        
        return ans
