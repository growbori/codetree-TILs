n = 4
arr = [1, 5, 2, 6]

count = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if arr[i] <=  arr[j] <= arr[k]:
                count += 1

print(count)