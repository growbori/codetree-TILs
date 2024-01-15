n = int(input())

for i in range(1, n):
    for j in range(i):
        print('*', end = ' ')
    print()

for i in range(n):
    for j in range(n-i):
        print('*', end = ' ')
    print()




# i 는 세로, j 는 가로