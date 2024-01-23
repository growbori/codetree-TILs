a, b = map(int, input().split())

arr=[a, b]

for i in range(2, 10):
    arr.append(arr[i-1] + arr[i-2])
for j in range(len(arr)):
    print(arr[j] % 10, end = ' ')