class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        width, height = len(board[0]), len(board)
        visited = set()
        
        def dfs(y, x, word_index=0):
#             print(y, x, word_index)
            if word_index == len(word):
                return True
            elif (x < 0) or (x == width) or (y < 0) or (y == height) or (word[word_index] != board[y][x]) or ((y, x) in visited):
                return False
            else:
                visited.add((y, x))
                result = (dfs(y-1, x, word_index+1) or dfs(y+1, x, word_index+1) or \
                          dfs(y, x-1, word_index+1) or dfs(y, x+1, word_index+1))
#                 print(y, x, "results: ", y-1, x,dfs(y-1, x, word_index+1) , y+1, x, dfs(y+1, x, word_index+1), \
#                           y, x-1,dfs(y, x-1, word_index+1) ,y, x+1, dfs(y, x+1, word_index+1))
                if result:
                    return True
                else:
                    visited.remove((y, x))
                    return False
                
        for i in range(height):
            for j in range(width):
                if dfs(i, j):
                    return True
        return False
