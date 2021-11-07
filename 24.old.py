# n = int(input())
# stroki = [input().lower() for i in range(n)]
#
# num = int(input())
# lst = [input().lower() for i in range(num)]
#
# count = 0
# new = []
#
# for i in range(n):
#     for j in range(num):
#         if lst[j] in stroki[i]:
#             count += 1
#     if count == num:
#         new.append(stroki[i])
#         count = 0
#
# print(new)

n = input().split('#')
num = int(n[-1])
lst = []
a = ''
lst3 = []

for i in range(num):
    stroka = input()
    if '#' in stroka:
        a = stroka.find('#')
        print(a)
    print(stroka[:a])
    stroka = ''

