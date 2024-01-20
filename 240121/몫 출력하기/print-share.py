cnt = 0
while True:

    n = int(input())

    if n % 2 != 0:
        continue
    else:
        if cnt >= 3:
            break
        print(int(n) //2)
        cnt += 1