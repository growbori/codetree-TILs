n = int(input())
summ = 0
for i in range(n):
    a = int(input())
    
    if a % 2 == 1 and a % 3 == 0:
        summ += a
        i += 1
print(summ)