class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited_set = set()
        max_area = 0
        height, width = len(grid), len(grid[0])
        
        def dfs(y, x):
            if ((y, x) in visited_set) or y < 0 or x < 0 or x >= width or y >= height or grid[y][x]==0:
                return 0
            else:
                visited_set.add((y, x))
                return 1+ dfs(y+1, x) + dfs(y-1, x) + dfs(y, x-1) + dfs(y, x+1)
            
        for i in range(height):
            for j in range(width):
                if (i, j) in visited_set:
                    continue
                else:
                    area = dfs(i, j)
                    max_area = max(max_area, area)
        
        return max_area
                
        
