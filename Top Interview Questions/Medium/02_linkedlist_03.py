class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stack_1 = []
        stack_2 = []
        
        ptr = headA
        while(ptr):
            stack_1.append(ptr)
            ptr = ptr.next
            
        ptr = headB
        while(ptr):
            stack_2.append(ptr)
            ptr = ptr.next
            
        current = None
        while stack_1 and stack_2:
            node_a = stack_1.pop()
            node_b = stack_2.pop()
            if node_a == node_b:
                current = node_a
            else:
                return current
        
        return current