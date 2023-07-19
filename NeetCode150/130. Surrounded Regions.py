class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        unflippable = set()
        rows, cols = len(board), len(board[0])
        
        def dfs(y, x):
            if (y, x) in unflippable or y < 0 or y == rows or x < 0 or x == cols or board[y][x] == 'X':
                return 
            else:
                unflippable.add((y, x))
                dfs(y+1, x)
                dfs(y-1, x)
                dfs(y, x+1)
                dfs(y, x-1)
                
        for i in range(cols):
            dfs(0, i)
            dfs(rows-1, i)
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols-1)
            
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and (i, j) not in unflippable:
                    board[i][j] = 'X'
        
        return board
