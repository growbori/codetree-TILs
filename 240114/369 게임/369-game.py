n = int(input())

for i in range(1, n+1):
    if i % 3 == 0:
        print(0, end = ' ')
    elif str(3) in str(i):
        print(0, end = ' ')
    elif str(6) in str(i):
        print(0, end = ' ')
    elif str(9) in str(i):
        print(0, end = ' ')
    else:
        print(i, end = ' ')