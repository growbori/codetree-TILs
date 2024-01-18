n = int(input())
cnt = 9
for i in range(n):
    for j in range(i):
        print(' ', end = ' ')
    for j in range(n-i):
        if 0 < cnt < 10:
            print(10-cnt, end = ' ')
            cnt -=1
        else:
            print(1, end = ' ')
            cnt += 8
    print()