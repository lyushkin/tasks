n = int(input())
d = {}
for i in range(n):
    word = input().split()
    d.setdefault(word[0], word[1])
word = input()

for k, v in d.items():
    if word == v:
        print(k)
    elif word == k:
        print(v)

