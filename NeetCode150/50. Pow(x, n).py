class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if n==0:
                return 1
            if n==1:
                return x
            elif n%2 == 0:
                half = helper(x, n//2)
                return half*half
            else:
                half = helper(x, n//2)
                return half*half*x
        ans = helper(x, abs(n))
        if n < 0:
            return 1/ans
        else:
            return ans
