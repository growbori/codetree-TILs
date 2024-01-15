arr = input().split()

a, b, c = int(arr[0]), int(arr[1]), int(arr[2])

satisfied = False

for i in range(a, b+1):
    if a % i == 0 and b % i == 0:
        satisfied = True

if satisfied == True:
    print('NO')
else:
    print('YES')