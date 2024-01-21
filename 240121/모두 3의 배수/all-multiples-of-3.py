cnt = 0

for _ in range(5):
    n = int(input())

    if n % 3 == 0:
        cnt += 1
    else:
        cnt += 0
    
if cnt < 5:
    print(0)
else:
    print(1)