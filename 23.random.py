import random
import string

# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
#
# for i in range(len(matrix)):
#     random.shuffle(matrix[i])
#
# print(matrix)


# slovo = input()
# print(*random.sample(slovo,len(slovo)), sep='')

# matrix = [[0] * 5 for i in range(5)]
# numbers = []
# a = 0
# while a != 24:
#     num = random.randint(1,75)
#     if num not in numbers:
#         numbers.append(num)
#         a += 1
# for i in range(5):
#     lst = []
#     for j in range(5):
#         if i == 2 == j:
#             matrix[i][j] = 0
#         else:
#             num = numbers.pop()
#             matrix[i][j] = num
#
# for i in range(5):
#     for j in range(5):
#         print(str(matrix[i][j]).ljust(3), end='')
#     print()
#4
#letters = []
# def generate_index():
#     index = ''
#     for i in range(9):
#         if i < 2 or i >= 7:
#             index += random.choice(string.ascii_uppercase)
#         elif i == 4:
#             index += '_'
#         else:
#             index += random.choice(string.digits)
#     return index
#
# print(generate_index())

#5
# lst = []
# for i in range(100):
#     stroka = random.randint(1000000, 9999999)
#     if stroka not in lst:
#         lst.append(stroka)
#
# print(*lst, sep='\n')

# n = int(input())
# lst = [input() for i in range(n)]
# lst2 = lst.copy()
# i = 0
# while lst[i] != lst2[i]:
#     random.shuffle(lst2)
#for i in range(len(lst)):
#    print(lst[i],'-', lst2[i])


