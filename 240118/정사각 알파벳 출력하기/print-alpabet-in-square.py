n = int(input())
num = 65
for i in range(n):
    for j in range(n):
        print(chr(num), end = '')
        num += 1
    print()