n = 3
queries = [[1,1,2,2],[0,0,1,1]]

matrix = [[0 for i in range(n)] for j in range(n)]

for r1,c1,r2,c2 in queries:
    matrix[r1][c1] += 1
    if r2+1 < n: matrix[r2+1][c1] += -1
    if c2+1 < n: matrix[r1][c2+1] += -1
    if r2+1 < n and c2+1 < n: matrix[r2+1][c2+1] += 1
print(*matrix, sep='\n')   
print()
for col in range(n):
    for row in range(1, n):
        matrix[row][col] += matrix[row-1][col]
print(*matrix, sep='\n')
print()
for row in range(n):
    for col in range(1, n):
        matrix[row][col] += matrix[row][col-1]
print(*matrix, sep='\n')