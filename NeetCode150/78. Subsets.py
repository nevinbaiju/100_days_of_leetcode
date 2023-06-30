

def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    ans = []

    def backtrack(i=0, curr_list=[]):
        
        if i == len(nums):
            ans.append(list(curr_list)) # Because .copy() does not work always.
            return
        
        curr_list.append(nums[i])
        backtrack(i+1, curr_list)

        curr_list.pop()
        backtrack(i+1, curr_list)

    backtrack()

    return ans

if __name__ == "__main__":
    nums = [1,2,3]
    print(subsets(nums))

        
        