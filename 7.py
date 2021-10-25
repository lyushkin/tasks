stroka = 'abcdefgh'
stolb = '87654321'
h = input().split()

y = stroka.index(h[0][0])
x = stolb.index(h[0][1])

matrix = [['.'] * 8 for _ in range(8)]
matrix[x][y] = 'N'

for i in range(8):
    for j in range(8):
        inx = (x - j) * (y - i)
        if inx == 2 or inx == -2:
            matrix[j][i] = '*'

for r in range(8):                     # выводим матрицу
    for c in range(8):
        print(matrix[r][c], end=' ')
    print()