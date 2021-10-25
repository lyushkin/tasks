row, col = int(input()), int(input())
matrix = []

for i in range(row):
    matrix.append(input().split())

lst = input().split()
n1, n2 = int(lst[0]), int(lst[1])
for i in range(1):
    for j in range(row):
        matrix[j][n1], matrix[j][n2] = matrix[j][n2], matrix[j][n1]

print(matrix)
