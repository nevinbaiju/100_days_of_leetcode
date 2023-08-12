"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        node_map = {}

        while curr:
            new_node = Node(curr.val)
            node_map[curr] = new_node
            curr = curr.next

        curr = head

        while curr:
            new_node = node_map[curr]
            new_node.next = node_map[curr.next] if curr.next else None
            new_node.random = node_map[curr.random] if curr.random else None
            curr = curr.next

        return node_map[head]
