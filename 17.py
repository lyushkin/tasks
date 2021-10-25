stroka = input()
d, symb = {}, {}
for i in range(int(input())):
    lst = input().split(': ')
    d.setdefault(lst[0], lst[1])

for i in stroka:
    symb[i] = symb.get(i, 0) + 1

for i in stroka:
    for k,v in d.items():
        if str(symb[i]) == v:
            print(k, end='')
