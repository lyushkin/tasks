n = int(input())
lst = []
for i in range(n):
    lst.append(input())
tup = tuple(lst)
print(*tup, sep='\n')
print()
for i in range(len(tup)):
    print(tup[i][-1])
    if int(tup[i][-1]) >= 4:
        print(tup[i])

