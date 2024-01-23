cntA = 0
cntB = 0
cntC = 0
cntD = 0
cnt = 0

for _ in range(3):
    n = input().split()
    a, b = n[0], int(n[1])

    if a == 'Y' and b >= 37:
        cntA +=1
        cnt += 1
    elif a == 'N' and b >= 37:
        cntB += 1
    elif a == 'Y' and b < 37:
        cntC += 1
    else:
        cntD += 1
if cnt >=2:
    emer = 'E'
else:
    emer = 'C'
print(cntA, cntB, cntC, cntD, emer)