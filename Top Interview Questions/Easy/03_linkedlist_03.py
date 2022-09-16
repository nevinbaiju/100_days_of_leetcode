class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_ll(nums):
    node = ListNode(nums[0])
    header = node
    ptr = header

    for i in range(1, len(nums)):
        node = ListNode(nums[i])
        ptr.next = node
        ptr = ptr.next

    return header

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        ptr = head
        prev_ptr = head
        ptr = prev_ptr.next
        prev_ptr.next = None

        while(ptr):
            temp = ptr.next
            ptr.next = prev_ptr
            prev_ptr = ptr
            ptr = temp

        return prev_ptr

if __name__ == "__main__":
    list_1 = [1,2,4, 1,3,4]

    ll_1 = create_ll(list_1)
    # while(ll_1):
    #     print(ll_1.val)
    #     ll_1 = ll_1.next
    # while(ll_2):
    #     print(ll_2.val)
    #     ll_2 = ll_2.next
    s = Solution()
    final_ll = s.reverseList(ll_1)

    ptr = final_ll

    while(ptr):
        print(ptr.val)
        ptr = ptr.next