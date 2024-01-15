a = int(input())

satisfied = False

for i in range(1, a+1):
    if a % i == 0:
        satisfied = True

if satisfied == True:
    print('C')
else:
    print('N')