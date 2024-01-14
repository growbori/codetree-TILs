n = int(input())
summ = 0
for i in range(1, 100+1):
    i += 1
    summ += i

    if summ >= n:
        break
    else:
        continue

print(i)