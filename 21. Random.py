#1
import random

#n = int(input())    # количество попыток
#s = ['Орел', 'Решка']
#for i in range(n):
#    print(random.choice(s))

#4
import random
s = []
i = 0
while i != 7:
    num = random.randint(1,49)
    if num not in s:
        s.append(num)
        i += 1
s.sort()
print(*s)
