class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        count = 0

        def dfs(node=root, max_val=root.val):
            nonlocal count

            if node:
                if node.val >= max_val:
                    count += 1
                new_max_val = max(max_val, node.val)
                dfs(node.left, new_max_val)
                dfs(node.right, new_max_val)
        dfs()
        
        return count
