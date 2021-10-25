n= int(input())
spisok = [input().split(': ') for i in range(n)]
n2 = int(input())
words = [input().lower() for i in range(n2)]
d = {}
for i in spisok:
    d.setdefault(i[0].lower(), i[1])
for i in words:
    print(d.get(i, "Не найдено"))


