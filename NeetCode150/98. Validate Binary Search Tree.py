class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node=root, left=-float('inf'), right=float('inf')):
            if node:
                if not (left < node.val < right):
                    return False
                return valid(node.left, left, node.val) and valid(node.right, node.val, right)
            else:
                return True
        
        return valid()
