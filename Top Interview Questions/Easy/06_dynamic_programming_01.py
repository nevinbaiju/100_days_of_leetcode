from functools import cache
from turtle import st
from typing import List
import time

class Solution:
    def climbStairs(self, n: int) -> int:
        def climb_recursion(steps_remaining):
            if steps_remaining == 0:
                return 1
            elif steps_remaining < 0:
                return 0
            else:
                return climb_recursion(steps_remaining-1) + climb_recursion(steps_remaining-2)

        cache = {}
        time1_start = time.time()
        ans = climb_recursion(n)
        print(time.time() - time1_start)


        def climb_dp(steps_remaining):

            # print(steps_remaining)
            if steps_remaining == 0:
                return 1
            elif steps_remaining < 0:
                return 0
            elif steps_remaining in cache:
                return cache[steps_remaining]
            else:
                steps_possible = climb_dp(steps_remaining-1) + climb_dp(steps_remaining-2)
                cache[steps_remaining] = steps_possible
                return steps_possible

        time_2_start = time.time()
        ans = climb_dp(n)
        print(ans)
        print(time.time() - time_2_start)
        print(cache)

        # return climb_dp(n) 


if __name__ == '__main__':
    params = 40
    s = Solution()
    s.climbStairs(params)
        