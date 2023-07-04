class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
            
        stack = []
        ans = []
        
        def backtrack(nums=list(nums)):
            if not nums:
                ans.append(list(stack))
            else:
                for i, num in enumerate(nums):
                    stack.append(num)
                    backtrack(list(nums[:i] + nums[i+1:]))
                    stack.pop()
        
        backtrack()
        return ans
