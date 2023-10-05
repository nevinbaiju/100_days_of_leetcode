class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = set()
        col_set = set()
        grid_set = set()
        
        def validate_row(row_num):
            if row_num in row_set:
                return True
            else:
                visited_set = set()
                for i in range(9):
                    if not board[row_num][i].isdigit():
                        continue
                    if board[row_num][i] in visited_set:
                        return False
                    else:
                        visited_set.add(board[row_num][i])
                row_set.add(row_num)
                return True
        
        
        def validate_col(col_num):
            if col_num in col_set:
                return True
            else:
                visited_set = set()
                for i in range(9):
                    if not board[i][col_num].isdigit():
                        continue
                    if board[i][col_num] in visited_set:
                        return False
                    else:
                        visited_set.add(board[i][col_num])
                col_set.add(col_num)
                return True
                
        def validate_grid(grid_num):
            if grid_num in grid_set:
                return True
            else:
                visited_set = set()
                row_grid_num = grid_num//3
                col_grid_num = grid_num%3
                for i in range(row_grid_num*3, (row_grid_num+1)*3):
                    for j in range(col_grid_num*3, (col_grid_num+1)*3):
                        if not board[i][j].isdigit():
                            continue
                        if board[i][j] in visited_set:
                            return False
                        else:
                            visited_set.add(board[i][j])
                    
                grid_set.add(grid_num)
                return True
        
        for i in range(9):
            for j in range(9):
                grid_num = (((i//3)*3)-1) + (j%3)
                if validate_row(i) and validate_col(j) and validate_grid(grid_num):
                    continue
                else:
                    print(i, j)
                    print(validate_row(i), validate_col(j), validate_grid(grid_num))
                    return False
        
        return True
