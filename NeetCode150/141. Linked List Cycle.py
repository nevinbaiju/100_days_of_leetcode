# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head and head.next:
            fast = head.next.next
        else:
            return False
        slow = head
        counter = 0 

        while slow and fast:
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next if fast.next else None

        return False
