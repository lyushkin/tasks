n = int(input())
matrix = [input().split() for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][i], matrix[n-(i+1)][i] = matrix[n-(i+1)][i], matrix[i][i]

for r in range(n):
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()
