slovo1 = input()
slovo2 = input()
slovar1, slovar2 = {},{}
for i in slovo1:
    slovar1[i] = slovar1.get(i, 0) + 1
for i in slovo2:
    slovar2[i] = slovar2.get(i, 0) + 1

if slovar1 == slovar2:
    print('YES')
else:
    print('NO')