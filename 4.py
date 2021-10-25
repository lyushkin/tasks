row, col = int(input()), int(input())
for i in range (row):
    if i % 2 == 0:
        for j in range(col):
            if j %2 == 0:
                print('.'.ljust(3), end='')
            else:
                print('*'.ljust(3), end='')
        print()
    else:
        for j in range(col):
            if j % 2 == 0:
                print('*'.ljust(3), end='')
            else:
                print('.'.ljust(3), end='')
        print()