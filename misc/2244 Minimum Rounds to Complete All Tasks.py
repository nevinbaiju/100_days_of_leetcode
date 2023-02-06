class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cache = {}
        def count_turns(num, count=0):
            if num == 0:
                return count
            elif num in cache:
                return cache[num] + 1
            elif num < 2:
                return float('inf')
            else:
                threes = count_turns(num-3, count+1)
                twos = count_turns(num-2, count+1)
                cache[num] = min(twos, threes)
                
                return min(twos, threes)
            
        tasks_count = {}

        for task in tasks:
            tasks_count[task] = tasks_count.get(task, 0) + 1
            
        total_turns = 0
        for task in tasks_count.keys():
            cache = {}
            turns = count_turns(tasks_count[task])
            if turns == float('inf'):
                return -1
            else:
                total_turns += turns
        return total_turns