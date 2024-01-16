n = int(input())

for i in range(2 * n):
    if i % 2 == 0:
        for j in range(n-int(0.5*i)):
            print('*', end = ' ')
        print()
    else:
        for k in range(i//2+1):
            print('*', end = ' ')
        print()