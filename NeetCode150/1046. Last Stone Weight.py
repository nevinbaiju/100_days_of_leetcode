import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            heapq._heapify_max(stones)
            a = stones.pop(0)
            heapq._heapify_max(stones)
            b = stones.pop(0)
            result = a - b
            if result:
                stones.append(result)
        if stones:
            return stones[0]
        else:
            return 0
