class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []

        new_left, new_right = newInterval
        for left_interval, right_interval in intervals:
            if new_left > right_interval:
                left += [[left_interval, right_interval]]
            elif new_right < left_interval:
                right += [[left_interval, right_interval]]
            else:
                print(new_left, left_interval)
                print(new_right, right_interval)
                new_left = min(new_left, left_interval)
                new_right = max(new_right, right_interval)

        ans = []
        if left:
            ans += left
        ans += [[new_left, new_right]]
        if right:
            ans += right
        return ans