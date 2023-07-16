import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_dict = Counter("".join(tasks))
        # print(count_dict)
        heap = [[count_dict[key], key] for key in count_dict.keys()]
        heapq._heapify_max(heap)

        cooldown_queue = []
        time = 0
        while heap or cooldown_queue:
            time += 1
        #     print(time)
            if heap:
                task_count, task = heap.pop(0)
                task_count -= 1
        #         print("Task: ", task)
                if task_count:
                    cooldown_queue.append([time+n, [task_count, task]])
            if cooldown_queue and time == cooldown_queue[0][0]:
                cooldown_time, task = cooldown_queue.pop(0)
                heap.append(task)
                heapq._heapify_max(heap)
        #     print(heap, cooldown_queue)
        #     print()
        return time
