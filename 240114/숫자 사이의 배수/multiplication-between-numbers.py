a, b = map(int, input().split())
summ = 0
count = 0
for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        summ += i
        count += 1

div = summ / count
print(summ, '%0.1f' %div)