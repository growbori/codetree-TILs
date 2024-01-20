cnt = 0
for _ in range(3):
    arr = input().split()
    a, b = arr[0], int(arr[1])

    if a == 'Y' and b >=37:
        answer = 'A'
        cnt += 1
    elif a == 'N' and b >= 37:
        answer = 'B'
    elif a == 'Y' and b < 37:
        answer = 'C'
    else:
        answer = 'D'

    if cnt >=2 :
        emer = 'E'
    else:
        emer = 'C'

print(emer)