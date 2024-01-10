class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count_dict = {}
        for i in range(m):
            count_dict[(i, 0)] = 1
        for i in range(n):
            count_dict[(0, i)] = 1
        for i in range(1, m):
            for j in range(1, n):
                count_dict[(i, j)] = count_dict[(i-1, j)] + count_dict[(i, j-1)]
        return count_dict[(m-1, n-1)]
