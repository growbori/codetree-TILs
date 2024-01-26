listarr = []
n = int(input())
for i in range(n):
    arr = input().split()
    listarr.append(arr)

a = ''.join(listarr[0])
b = ''.join(listarr[1])
c = ''.join(listarr[2])

length = len(a) + len(b) + len(c)

a1 = a.count('a')
a2 = b.count('a')
a3 = c.count('a')

conn = a1 + a2 + a3
print(length, conn)