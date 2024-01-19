n = int(input())
cnt = 0
for i in range(1, 101):
    if n < 1000:
        if n % 2 == 0:
            n= 3 * n + 1
            cnt += 1
        else:
            n = 2 * n + 2
            cnt += 1
    else:
        break
print(cnt)