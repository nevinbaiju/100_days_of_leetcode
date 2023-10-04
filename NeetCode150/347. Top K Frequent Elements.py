class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
        count_heap = [(count_dict[key], key) for key in count_dict.keys()]
        heapq._heapify_max(count_heap)
        sol = []
        for i in range(k):
            sol.append(heapq._heappop_max(count_heap)[1])
        return sol
