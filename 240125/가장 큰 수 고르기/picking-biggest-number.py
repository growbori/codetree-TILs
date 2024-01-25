arr = list(map(int, input().split()))
maxnum = 0
for i in range(len(arr)):
    if arr[i] > maxnum:
        maxnum = arr[i]

print(maxnum)