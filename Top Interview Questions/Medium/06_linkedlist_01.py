from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:

        end_index = len(nums) - 1
        def try_jumping(index):
            if index == end_index:
                return True
            elif index > end_index:
                return False

            max_jumps = nums[index]

            if max_jumps:
                for i in range(1, max_jumps+1):
                    can_reach = try_jumping(index + i)
                    if can_reach:
                        return True
                    else:
                        return False
            else:
                return False
        
        cache = {}

        def try_jumping_dp(index):
            if index == end_index:
                return True
            elif index > end_index:
                return False

            if index in cache:
                print('used cache')
                return cache[index]

            max_jumps = nums[index]
            can_reach = False
            for i in range(1, max_jumps+1):
                can_reach = try_jumping_dp(index + i)
                cache[index] = can_reach
                
                if can_reach:
                    break
            
            return can_reach

        ans = try_jumping_dp(0)
        print(cache)
        return ans



if __name__ == '__main__':
    params = [1, 1, 1, 1, 1, 6, 0, 0, 0, 0, 1]

    s = Solution()
    print(s.canJump(params))
          