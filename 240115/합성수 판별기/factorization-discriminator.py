a = int(input())

satisfied = False

for i in range(2, a):
    if a % i == 0:
        satisfied = True

if satisfied == True:
    print('C')
else:
    print('N')