class Solution(object):
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        deletion = head
        ptr = head
        counter = 1
        while ptr:
            if counter > n:
                prev = prev.next
                deletion = deletion.next
            counter += 1
            ptr = ptr.next
        print(prev, deletion)
        prev.next = deletion.next
        
        return dummy.next
