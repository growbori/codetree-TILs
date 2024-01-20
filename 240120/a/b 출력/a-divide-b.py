a, b = map(int, input().split())
c = a/b

if len(str(a/b)) < 20:
    print(str(a/b)+'0'*(22-len(str(a/b))))
else:
    print('{%0.20f}' %c)