n = int(input())

for i in range(2*n):
    if i % 2 == 1:
        for j in range(int(n-(i-1)/2)):
            print('*', end =' ')
        print()
    else:
        for j in range(1+int(i/2)):
            print('*', end =' ')
        print()