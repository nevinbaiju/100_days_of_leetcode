class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        sol = [0]*(len(cost))
        sol[-2] = cost[-2]
        for i in range(len(cost)-3, -1, -1):
            sol[i] = cost[i] + min(sol[i+1], sol[i+2])
        
        return min(sol[0], sol[1])
                
                
