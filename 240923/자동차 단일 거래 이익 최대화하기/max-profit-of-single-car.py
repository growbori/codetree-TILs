n = int(input())

arr = list(map(int, input().split()))


check = []
for i in range(n):
    for j in range(i, n):
        front = arr[i]
        back = arr[j]
        ans = back - front
        check.append(ans)

if max(check) > 0:
    print(max(check))
else :
    print(0)