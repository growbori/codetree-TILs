summ = 0
count = 0
while True:
    n = int(input())

    if 19 < n < 30:
        summ += n
        count += 1
        continue
    else:
        break

print(f'{summ/count:.2f}')