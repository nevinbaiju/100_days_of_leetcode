class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        num_stations = len(gas)
        diff = [gas[i]-cost[i] for i in range(num_stations)]
        curr_diff = 0
        curr_ans = None
#         print(diff)
        for i in range(num_stations):
#             print(curr_ans, curr_diff, i)
            if curr_diff + diff[i] < 0:
#                 print("reset")
                curr_ans = None
                curr_diff = 0
            else:
                curr_diff += diff[i]
                if curr_ans is None:
                    curr_ans = i
        return curr_ans
