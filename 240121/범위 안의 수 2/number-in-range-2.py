summ = 0
count = 0

for i in range(10):
    i = input()

    if 0 <= int(i) <= 200:
        summ += int(i)
        count += 1
        avg = summ / count
print(summ, '%0.1f' %avg)