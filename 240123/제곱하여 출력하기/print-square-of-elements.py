n = int(input())

arr = list(map(int, input().split()))

for i in range(len(arr)):
    print(arr[i] ** 2, end = ' ')