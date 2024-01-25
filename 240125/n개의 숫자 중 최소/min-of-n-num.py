n = int(input())

arr = list(map(int, input().split()))

minnum = arr[0]

for i in range(len(arr)):
    if minnum > arr[i]:
        minnum = arr[i]
count = arr.count(minnum)
print(minnum, count)