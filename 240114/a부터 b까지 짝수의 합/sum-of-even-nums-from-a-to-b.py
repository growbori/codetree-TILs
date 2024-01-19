a, b = map(int, input().split())
summ =0
for i in range(a, b+1):
    if i % 2 == 0:
        summ += i
print(summ)