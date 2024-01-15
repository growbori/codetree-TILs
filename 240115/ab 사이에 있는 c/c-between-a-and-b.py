arr = input().split()

a,b,c = int(arr[0]), int(arr[1]), int(arr[2])

satisfied = False
for i in range(a, b + 1):
    if i % c == 0:
        satisfied = True

if satisfied == True:
    print('YES')
else:
    print('NO')