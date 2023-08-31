class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = []
        l = r = 0
        ans = []
        while r < len(nums):
            while deque and deque[-1] < nums[r]:
                deque.pop()
            deque.append(nums[r])
            r += 1
            if (r-l) == k:
                ans.append(deque[0])
                if nums[l] == deque[0]:
                    deque.pop(0)
                l += 1

        return ans
