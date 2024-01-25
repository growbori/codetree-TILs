arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 999 or arr[i] == -999:
        break

maxnum = arr[0]

for i in range(1, len(arr)-1):
    if arr[i] > maxnum:
        maxnum = arr[i]


        
print(maxnum, min(arr))