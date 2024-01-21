a, b, c = map(int, input().split(' '))

answer = True

for i in range(a, b+1):
    if i % c != 0:
        answer = True
    else:
        answer = False

if answer == True:
    print('YES')
else:
    print('NO')