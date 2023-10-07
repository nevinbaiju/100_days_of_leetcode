class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = 0
        max_r = 0
        l, r = 0, len(height)-1
        ans = 0
        
        while (l != r):
            if height[l] < height[r]:
                ans += max(0, max_l-height[l])
                max_l = max(max_l, height[l])
                l += 1
            else:
                ans += max(0, max_r-height[r])
                max_r = max(max_r, height[r])
                r -= 1 
        
        return ans
