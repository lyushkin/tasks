d = {}
for i in range(int(input())):
    spisok = input().split()
    d.setdefault(spisok[0], spisok[1:])
words = [input() for i in range(int(input()))]

for i in words:
    for k, v in d.items():
        if i in v:
            print(k)
