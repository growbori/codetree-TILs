n = int(input())

arr = list(map(int, input().split()))

profit = 0
min_cost  = min(arr)
c = 0
for i in range(n):
    if arr[i] == min_cost:
        c = i

check = []
for j in range(c, n):
    check.append(arr[j])

if len(check) == 1:
    print(0)
else :
    max_cost = max(check)
    print(max_cost - min_cost)