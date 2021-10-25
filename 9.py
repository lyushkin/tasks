num = input().split()
row, col = int(num[0]), int(num[1])
matrix, count = [], 0

for i in range(row):
    lst = []
    for j in range(col):
        count += 1
        lst.append(count)
    matrix.append(lst)

for i in range(len(matrix)):
    if i % 2 != 0:
        lst = matrix[i][::-1]
        matrix[i] = lst

for r in range(row):
    for c in range(col):
        print(matrix[r][c], end=' ')
    print()