# Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            prev = head
            ptr = head.next
            prev.next = None
        else:
            return head
        
        while ptr:
            curr_node = ptr
            ptr = ptr.next
            curr_node.next = prev
            prev = curr_node
        return prev
