class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.'] * n for _ in range(n)]
        col_set = set()
        pos_diag_set = set()
        neg_diag_set = set()
        
        def dfs(row=0):
            if row == n:
                curr_ans = ["".join(row) for row in board]
                ans.append(list(curr_ans))
            else:
                for col, spot in enumerate(board[row]):
                    if (col in col_set) or ((row-col) in pos_diag_set) or ((row+col) in neg_diag_set):
                        continue
                    else:
                        col_set.add(col)
                        pos_diag_set.add(row-col)
                        neg_diag_set.add(row+col)
                        board[row][col] = 'Q'
#                         print(row, col)
#                         print(*board, sep='\n')
#                         print("")
                        dfs(row+1)
                        col_set.remove(col)
                        pos_diag_set.remove(row-col)
                        neg_diag_set.remove(row+col)
                        board[row][col] = '.'
        dfs()
        return ans
