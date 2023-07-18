"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        created_dict = {}

        def copy_dfs(node):
            new_node = Node(node.val)
            created_dict[node.val] = new_node
            for neighbor in node.neighbors:
                if neighbor.val in created_dict:
                    new_node.neighbors.append(created_dict[neighbor.val])
                else:
                    neighbor_node = copy_dfs(neighbor)
                    new_node.neighbors.append(neighbor_node)

            return new_node

        if node:
            copied_node = copy_dfs(node)
            return copied_node
        else:
            return None
