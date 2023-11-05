class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        a = 1
        b = 2
        c = a+b
#         print(1, a)
#         print(2, b)
        for i in range(3, n+1):
            c = a+b
            a = b
            b = c
#             print(i, c)
#         print(a, b, c)
        return c
