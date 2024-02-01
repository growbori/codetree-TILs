arr = input().split()

a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

satisfied = True

for i in range(a, b+1):
    if i % c != 0:
        satisfied = False
    else:
        satisfied = True

if satisfied == False:
    print('YES')
else:
    print('NO')