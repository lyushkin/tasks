num = input().split()
stroka, stolbec = int(num[0]), int(num[1])
matrix1, matrix2, matrix_sum = [], [], []

for i in range(stroka):
    numbers = input().split()
    matrix1.append(numbers)

s = input()

for i in range(stroka):
    numbers = input().split()
    matrix2.append(numbers)

for i in range(stroka):
    d = []
    for j in range(stolbec):

        d.append(int(matrix1[i][j])+int(matrix2[i][j]))
    matrix_sum.append(d)

for s in range(stroka):                     # выводим матрицу
    for st in range(stolbec):
        print(matrix_sum[s][st], end=' ')
    print()