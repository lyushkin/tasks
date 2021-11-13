# stroka = input().split()
# n = int(input())
# matrix, temp = [], []
#
# for i in range(n):
#     matrix.append(stroka[i::n])
# print(matrix)

#2
# n = int(input())
# matrix = [[0] * n for _ in range(n)]
#
# for i in range(n):
#     matrix[i] = input().split()
# maximum = int(matrix[0][0])
# for i in range(n):
#     for j in range(n):
#         if (i <= j and i > n - 1 - j) or (i >= j and i >= n - 1 - j):
#             if int(matrix[i][j]) > maximum:
#                 maximum = int(matrix[i][j])
#
# print(maximum)

#3
# n = int(input())
# matrix = []
# matrix2 = [[0] * n for _ in range(n)]
# for i in range(n):
#     matrix.append(input().split())
#
# for i in range(n):
#     for j in range(n):
#         matrix2[i][j] = matrix[j][i]
#
# for r in range(n):
#     for c in range(n):
#         print(matrix2[r][c], end=' ')
#     print()

#4

# n = int(input())
# matrix = []
#
# for i in range(n):
#     temp = []
#     for j in range(n):
#         if i == j or i + j + 1 == n or j == n // 2 or i == n // 2:
#             temp.append('*')
#         else:
#             temp.append('.')
#     matrix.append(temp)
#
# for r in range(n):
#      for c in range(n):
#          print(matrix[r][c], end=' ')
#      print()

#5

# n = int(input())
# matrix = []
# matrix2 = [[0] * n for _ in range(n)]
# for i in range(n):
#     matrix.append(input().split())
#
# for i in range(n):
#     for j in range(n):
#         matrix2[i][j] = matrix[j][i]
#
# for i in range(n):
#         matrix2[n - 1 - i].reverse()
#         if matrix[i] == matrix2[n-1-i]:
#             flag = 'YES'
#         else:
#             flag = 'NO'
#
# print(flag)

n = int(input())
matrix = [input().split() for i in range(n)]
for i in range(n):
    matrix[i] = set(matrix[i])

for i in range(1, n+1):
    if matrix[0] == matrix[n-i]:
        flag = 'YES'
    else:
        flag = 'NO'
        break
print(flag)