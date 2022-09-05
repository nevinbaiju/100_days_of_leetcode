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
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = None

        if not list1:
            if not list2:
                return None
            else:
                return list2
        elif not list_2:
            return list1

        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        ptr_1 = list1
        ptr_2 = list2
        final_ptr = head

        while(ptr_1 and ptr_2):
            if ptr_1.val <= ptr_2.val:
                final_ptr.next = ptr_1
                ptr_1 = ptr_1.next
                final_ptr = final_ptr.next
            else:
                final_ptr.next = ptr_2
                ptr_2 = ptr_2.next
                final_ptr = final_ptr.next
        
        if(ptr_1):
            final_ptr.next = ptr_1
        if(ptr_2):
            final_ptr.next = ptr_2
        return head

if __name__ == "__main__":
    list_1 = [1,2,4]
    list_2 = [1,3,4]

    ll_1 = create_ll(list_1)
    ll_2 = create_ll(list_2)
    # while(ll_1):
    #     print(ll_1.val)
    #     ll_1 = ll_1.next
    # while(ll_2):
    #     print(ll_2.val)
    #     ll_2 = ll_2.next
    s = Solution()
    final_ll = s.mergeTwoLists(ll_1, ll_2)

    ptr = final_ll

    while(ptr):
        print(ptr.val)
        ptr = ptr.next