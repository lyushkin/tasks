#1
#my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21], 'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42], 'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
#for k,v in my_dict.items():
#    for i in v:
#        if i > 20:
#            v.remove(i)
#print(my_dict)

#2
#emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#         'yandex.ru': ['surface', 'google'],
#         'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#         'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
#new =[]
#for k,v in emails.items():
#    for i in v:
#        new.append(i + '@' + k)
#print(*sorted(new), sep='\n')

#3
# slovar = {'G':'C','C':'G','T':'A','A':'U'}
# stroka = input()
# for i in stroka:
#     print(slovar[i],end='')

#4
# stroka = input().split()
# result = {}
#
# for i in stroka:
#     result[i] = result.get(i, 0) + 1
#     print(result[i], end=' ')

#5
# letters = {1: ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U'], 2: ['D', 'G'], 3: ['B', 'C', 'M', 'P'],
#            4: ['F', 'H', 'V', 'W', 'Y'], 5: ['K'], 8: ['J', 'X'], 10: ['Q', 'Z']}
# stroka = input().split()
# sum = 0
# for i in stroka:
#     for k, v in letters.items():
#         if i in v:
#             sum += k
# print(k)

#6
# stroka = []
# slovar = {'name': 'timur', 'age': 28}
# for k,v in slovar.items():
#     temp = str(k)+ '='+ str(v)
#     stroka.append(temp)
# stroka.sort()
#
# print('&'.join(stroka))

#7
# slovar = [{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]
#
# result = {}
# for i in slovar:
#     for k,v in i.items():
#         if k in result:
#             result[k].add(v)
#         else:
#             result[k] = {v}
#
# print(result)

#8
# d = {}
# for i in range(int(input())):
#     a, b, c = input().split()
#     d[a] = d.get(a, {})
#     d[a][b] = d.get(a, {}).get(b, 0) + int(c)
# for i in sorted(d):
#     print(f'{i}:', sep='\n')
#     for k in sorted(d[i]):
#         print(f'{k} {d[i][k]}', sep='\n')



#9
kod = {'read': 'R',
    'write': 'W',
    'execute': 'X',}
d = {}
for i in range(int(input())):
    file, *a = input().split()
    d[file] = set(a)

for i in range(int(input())):
    action, file = input().split()
    if kod[action] in d[file]:
        print('OK')
    else:
        print('Access denied')

# print('OK')
# print("Acess denied")
