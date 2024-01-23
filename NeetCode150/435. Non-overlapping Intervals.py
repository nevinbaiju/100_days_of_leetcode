class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        last = intervals[0]
        ans = 0
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < last[1]:
                last[1] = min(last[1], intervals[i][1])
                ans += 1
            else:
                last = intervals[i]
        
        return ans
