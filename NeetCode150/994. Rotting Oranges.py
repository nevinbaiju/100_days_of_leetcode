class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        minutes_to_rot = [[float('inf')]*cols for _ in range(rows)]
        visited = set()
        
        def dfs(y, x, minutes=0):
            if (y, x) in visited or y < 0 or y == rows or x < 0 or x == cols or grid[y][x] == 0 or grid[y][x] == 0 or minutes > minutes_to_rot[y][x]:
#                 print(y, x, minutes)
                return
            else:
                visited.add((y, x))
#                 print(visited)
#                 print(*minutes_to_rot, end='\n')
                minutes_to_rot[y][x] = minutes
                dfs(y+1, x, minutes+1)
                dfs(y-1, x, minutes+1)
                dfs(y, x+1, minutes+1)
                dfs(y, x-1, minutes+1)
                visited.remove((y, x))
        
        for i in range(rows):
            for j in range(cols):
                visited = set()
                if grid[i][j] == 2:
                    dfs(i, j)
#                     print()
        
        total_mins = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and total_mins < minutes_to_rot[i][j]:
                    total_mins = minutes_to_rot[i][j]
        
        if total_mins == float('inf'):
            return -1
        else:
            return total_mins
        
