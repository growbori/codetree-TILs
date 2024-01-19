a = 0
b = 0
c = 0

n = int(input())
for i in range(1, n+1):
    if i % 2 == 0 and i % 6 != 0 and i % 12 != 0:
        a += 1

    elif i % 3 == 0 and i % 12 != 0:
        b += 1
    
    elif i % 12 == 0:
        c += 1

print(a, b, c)