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


# # комментарии, строки
# n = input().split('#')
# num = int(n[-1])
# lst = []
# a = 0
#
# for i in range(num):
#     stroka = input()
#     if '#' in stroka:
#         a = stroka.find('#')
#         new = stroka[:a]
#         new = new.rstrip()
#         lst.append(new)
#     else:
#         lst.append(stroka)
#
# print(*lst, sep='\n')
#
#
# a, b = int(input()), int(input())
# summa, temp = 0, 0
# number = 0
# for i in range(a, b+1):
#     for j in range(1,i+1):
#         if i % j == 0:
#             temp += j
#     if temp > summa:
#         summa = temp
#         temp = 0
#         number = i
#
# print(number, summa)


#
# n = int(input())
# lst = []
# for i in range(n):
#     temp = [int(i) for i in input().split()]
#     lst.extend(temp)
# lst.sort()
# print(lst)


# объявление функции




def is_valid_password(password):
    password = [int(i) for i in password.split(":")]

    def is_prime(num):
        if num == 1:
            return False
        for i in range(2, password[1]):
            if num % i == 0:
                return False
        return True


    a = str(password[0])[::-1]
    b = password[1]
    c = password[2] % 2
    print()
    if 3 > len(password) > 3:
         return False
    # elif a == password[0] and c % 2 == 0;
    # return True


# считываем данные
psw = '1221:101:22'

# вызываем функцию
print(is_valid_password(psw))





