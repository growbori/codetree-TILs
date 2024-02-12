a, b = input().split()
count = 0
for _ in range(int(a)):
    string = input()
    
    if b == string:
        count += 1
print(count)