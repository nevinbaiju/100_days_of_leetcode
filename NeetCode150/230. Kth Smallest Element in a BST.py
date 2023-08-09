class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node = root
        curr_k = 0
        stack = []
        ans = None

        while curr_k < k:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                curr_k += 1
                node = stack.pop()
                ans = node.val
                node = node.right
        
        return ans
