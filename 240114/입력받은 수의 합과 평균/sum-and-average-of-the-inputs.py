n = int(input())
summ = 0
i = 0
for i in range(n):
    a = int(input())
    summ += a
    i += 1
div = summ / i
print(summ, '%0.1f' %div)