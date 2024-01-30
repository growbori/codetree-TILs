n = int(input())
arr = list(input().split())

result = []
for i in range(len(arr)):
    k = 0
    for j in range(len(arr)):
        if j != i:
            k += int(arr[j]) * abs(j - i)
    result.append(k)
print(min(result))