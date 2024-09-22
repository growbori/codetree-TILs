N, M = map(int, input().split())
arr = list(map(int, input().split()))
check = list(map(int, input().split()))

count = 0
for i in range(N):
    if arr[i:i+M] == check:
        count += 1

if count == 0:
    print("No")
else :
    print("Yes")