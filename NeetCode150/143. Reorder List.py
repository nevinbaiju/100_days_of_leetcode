class Solution(object):
    
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        stack = []
        queue = []
        ptr = head
        while ptr:
            stack.append(ptr)
            ptr = ptr.next
        
        counter = 0
        dummy = ListNode(None)
        ptr = dummy
        
        while stack:
            print(stack, counter)
            if counter % 2 == 0:
                node = stack.pop(0)
                node.next = None
                ptr.next = node
            else:
                node = stack.pop()
                node.next = None
                ptr.next = node
            ptr = ptr.next
            counter += 1
            
        return dummy.next
