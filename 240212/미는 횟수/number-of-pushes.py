a = input()
b = input()


for i in range(len(a)):
    c = a[i:] + a[:i]
    if c == b:
        print(i)