class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        height, width = len(grid), len(grid[0])
        visited = [[False] * width for _ in range(height)]
        
        def dfs(y, x):
            if (x < 0) or (y < 0) or (x >= width ) or (y >= height) or visited[y][x] or grid[y][x] == "0":
                return
            else:
                visited[y][x] = True
                dfs(y-1, x)
                dfs(y+1, x)
                dfs(y, x-1)
                dfs(y, x+1)
        
        islands = 0
        
        for i in range(height):
            for j in range(width):
                if visited[i][j] or grid[i][j] == "0":
                    continue
                else:
                    dfs(i, j)
                    islands += 1
        return islands
