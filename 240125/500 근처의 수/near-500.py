arr = list(map(int, input().split()))


maxnum = 0
for i in range(10):
    if maxnum < arr[i] and arr[i] < 500:
        maxnum = arr[i]

minnum = 0
for i in range(10):
    if minnum < arr[i] and arr[i] > 500:
        minnum = arr[i]

print(maxnum, minnum)