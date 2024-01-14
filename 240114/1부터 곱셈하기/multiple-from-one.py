n = int(input())
mul = 1
for i in range(1, 10+1):
    mul *= i
    i += 1
    if mul >= n:
        break
    else:
        continue

print(i-1)