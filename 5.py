n = int(input())
matrix = [[0]*n for _ in range(n)]
for i in range(n):
    matrix[i][n-i-1] = 1

for i in range(n):
    for j in range(n):
        if (j >= i > n - 1 - j) or (i >= j and i > n - 1 - j):
            matrix[i][j] = 2

for r in range(n):                     # выводим матрицу
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()