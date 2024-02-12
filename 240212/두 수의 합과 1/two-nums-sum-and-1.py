a, b = map(int, input().split())

c = a+b
count = 0
for i in str(c):
    if '1' in i:
        count += 1
print(count)