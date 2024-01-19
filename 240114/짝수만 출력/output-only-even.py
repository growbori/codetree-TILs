a, b = map(int, input().split())
i = a
while i <=b:
    if i % 2 == 0:
        print(i, end = ' ')
        i +=2
    else:
        print(i+1, end = ' ')
        i += 2