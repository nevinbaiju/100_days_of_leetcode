from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache  = {}
        def take_path(current_m, current_n):
            if (current_m == m-1) and (current_n == n-1):
                return 1
            elif (current_m, current_n) in cache:
                return cache[(current_m, current_n)]
            
            paths_possible = 0
            if current_m < m-1:
                paths_possible += take_path(current_m+1, current_n)
            if current_n < n-1:
                paths_possible += take_path(current_m, current_n+1)
                
            cache[(current_m, current_n)] = paths_possible
            return paths_possible
        
        return take_path(0, 0)

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(*(7, 3)))