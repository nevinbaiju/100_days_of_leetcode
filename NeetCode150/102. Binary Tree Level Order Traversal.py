# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [root]
        temp_stack = []

        ans = []

        while stack:
            curr_ans = []
            for node in stack:
                if node:
                    temp_stack.append(node.left)
                    temp_stack.append(node.right)
                    curr_ans.append(node.val)
            stack = temp_stack
            temp_stack = []
            if curr_ans:
                ans.append(curr_ans)

        return ans
