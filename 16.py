d = {}
for i in range(int(input())):
    spisok = input().split()
    d.setdefault(spisok[0], spisok[1])
words = [input().title() for i in range(int(input()))]

for i in words:
    lst = []
    for k, v in d.items():
        if i == v:
            lst.append(k)
    if lst != []:
        print(*lst)
    elif lst == []:
        print('абонент не найден')

