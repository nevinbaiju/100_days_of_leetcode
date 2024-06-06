class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x:x[0])
        a, b, ans = 0,0, 0
        for i in range(0, len(meetings)) :
            if b < meetings[i][0] :
                ans += meetings[i][0]-b - 1
                a, b = meetings[i]
            else :
                b = max(b, meetings[i][1])
        return ans + days-b
