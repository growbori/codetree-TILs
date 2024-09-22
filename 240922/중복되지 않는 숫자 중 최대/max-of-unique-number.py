n = int(input())

arr = list(map(int, input().split()))
maxnum = -1
blank = [0] * 1000

for i in range(n):
    if maxnum <= arr[i]:
        blank[arr[i]] += 1
check = []
for j in range(1000):
    if blank[j] == 1:
        check.append(j)

if len(check) != 0:
    print(check[-1])
else :
    print(-1)