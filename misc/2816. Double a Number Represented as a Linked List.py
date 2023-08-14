class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        ptr = head
        
        while ptr:
            stack.append(ptr)
            ptr = ptr.next
            
        carry = 0
        while stack:
            node = stack.pop()
            ans = 2 * node.val + carry
            node.val = ans % 10  
            carry = ans // 10
        
        if carry:
            new_node = ListNode(carry, head)
            head = new_node
            
        return head
