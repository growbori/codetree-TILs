a, b = map(int, input().split())
count = 0
for i in range(a, b+1):
    if ('3' in str(i)) or ('6' in str(i)) or ('9' in str(i)) or i % 3 == 0:
        count += 1 

print(count)