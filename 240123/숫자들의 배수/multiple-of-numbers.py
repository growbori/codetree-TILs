n = int(input())
cnt = 0
for i in range(1, 100):

    if n*i % 5 == 0:
        cnt += 1
    if cnt == 2:
        print(n*i)
        break
    else:
        print(n*i, end = ' ')