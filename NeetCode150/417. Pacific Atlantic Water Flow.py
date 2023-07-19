class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        atl = set()
        pac = set()
        rows, cols = len(heights), len(heights[0])
        
        def dfs(row, col, visit_set, prev_height):
            if (row, col) in visit_set or (row < 0) or (row >= rows) or (col < 0) or (col >= cols) or (heights[row][col] < prev_height):
                return
            else:
                visit_set.add((row, col))
                dfs(row-1, col, visit_set, heights[row][col])
                dfs(row+1, col, visit_set, heights[row][col])
                dfs(row, col-1, visit_set, heights[row][col])
                dfs(row, col+1, visit_set, heights[row][col])
        
        for i in range(cols):
            dfs(0, i, pac, heights[0][i])
            dfs(rows-1, i, atl, heights[rows-1][i])
        
        for i in range(rows):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, cols-1, atl, heights[i][cols-1])
            
        results = []
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) in atl and (i, j) in pac:
                    results.append([i, j])
                    
        return results
