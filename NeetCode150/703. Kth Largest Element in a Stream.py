import heapq

from queue import PriorityQueue

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            self.heap.pop(0)
            
    def add(self, val: int) -> int:
        self.heap.append(val)
        heapq.heapify(self.heap)
        if len(self.heap) > self.k:
            self.heap.pop(0)
            heapq.heapify(self.heap)
        return self.heap[0]
