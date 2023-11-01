class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        visited_rows = set()
        visited_cols = set()
        num_rows, num_cols = len(matrix), len(matrix[0])
        def set_zero(row, col, num_rows=num_rows, num_cols=num_cols):
            if col not in visited_cols:
                for i in range(num_rows):
                    matrix[i][col] = 0
                visited_cols.add(col)
                
            if row not in visited_rows:
                for j in range(num_cols):
                    matrix[row][j] = 0
                visited_rows.add(row)
        zero_indices = []
        
        for i in range(num_rows):
            for j in range(num_cols):
                if not matrix[i][j]:
                    zero_indices.append([i, j])
#         print(*matrix, end='\n\n', sep='\n')
        for i, j in zero_indices:
            set_zero(i, j)
#             print(*matrix, end='\n', sep='\n')
#             print(visited_rows, visited_cols)
#             print()
#         print(zero_indices)
        return matrix
        
        
