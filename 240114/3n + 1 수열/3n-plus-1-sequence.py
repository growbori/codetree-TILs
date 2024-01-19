n = int(input())
i = 0
while True:
    if n == 1:
        break
    if n % 2 == 0:
        n = n//2
        i += 1
    else:
        n = 3 * n + 1
        i += 1
    
print(i)