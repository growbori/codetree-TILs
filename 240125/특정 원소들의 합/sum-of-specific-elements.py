n = 4
arr2 = []
for i in range(4):
    arr = list(map(int, input().split()))
    arr2.append(arr)


sum_val = 0

for i in range(4):
    for j in range(i + 1):
        sum_val += arr2[i][j]
print(sum_val)