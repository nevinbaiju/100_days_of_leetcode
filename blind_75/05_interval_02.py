class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda interval: interval[0])
        ans = []
        for interval in intervals:
            if ans and interval[0] <= ans[-1][1]:
                ans[-1][1] = max(interval[1], ans[-1][1])
            else:
                ans += [interval]
                
        return ans
                    