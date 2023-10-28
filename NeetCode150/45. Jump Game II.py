class Solution:
    def jump(self, nums: List[int]) -> bool:
        queue = [0]
        jumps = 0
        searching = True
        while searching:
            temp_queue = set()
            while queue:
                curr = queue.pop()
                if curr == len(nums)-1:
                    searching = False
                    break
                for i in range(curr+1, min(len(nums), curr+nums[curr]+1)):
                    temp_queue.add(i)
            queue = list(temp_queue)
            if searching:
                jumps += 1
            else:
                break
        return jumps
