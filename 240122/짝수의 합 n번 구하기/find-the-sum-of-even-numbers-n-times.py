n = int(input())

for _ in range(n):
    arr = input().split()
    a, b = int(arr[0]), int(arr[1])
    summ = 0
    for i in range(a, b+1):
        if i % 2 == 0:
            summ += i
    print(summ)