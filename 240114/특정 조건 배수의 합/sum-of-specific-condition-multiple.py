a, b = map(int, input().split())

count = 0
if a < b:
    for i in range(a, b+1):
        if i % 5 == 0:
            count += i

    print(count)

if a > b:
    for i in range(b, a+1):
        if i % 5 == 0:
            count += i

    print(count)