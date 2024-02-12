a, b = input().split()

for _ in range(int(a)):
    string = input()
    count = 0
    if b == string:
        count += 1
        print(count)