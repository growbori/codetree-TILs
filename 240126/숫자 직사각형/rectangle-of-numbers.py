a, b = map(int, input().split())
cnt = 1
for i in range(a):
    for j in range(b):
        print(cnt, end = ' ')
        cnt+=1
    print()