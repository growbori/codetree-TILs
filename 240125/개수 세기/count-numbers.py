a, b = map(int, input().split())

arr = list(map(int, input().split()))

# print(arr)

for i in range(len(arr)):
    cnt = arr.count(b)

print(cnt)