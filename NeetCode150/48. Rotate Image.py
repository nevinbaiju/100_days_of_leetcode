class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp = [list(row) for row in matrix]
        size = len(temp)
        
        for i in range(size):
            for j in range(size):
                matrix[j][size-1-i] = temp[i][j]
