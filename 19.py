n, m = [int(i) for i in input().split()]
mtrx1 = [[int(i) for i in input().split()] for i in range(n)]
input()
m, k = [int(i) for i in input().split()]
mtrx2 = [[int(i) for i in input().split()] for i in range(m)]

mtrx3 = []


num = 0
for i in range(m):
    for j in range(k):
        num += mtrx1[i][j]*mtrx2[i][j]
    mtrx3[i][j] = num



print(mtrx3)