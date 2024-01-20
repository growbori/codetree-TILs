n = int(input())


if n % 4 ==0 and n % 100 == 0:
    print('false')
elif n % 4 == 0 and n % 100 == 0 and n % 400 == 0:
    print('true')
elif n % 4 == 0:
    print('true')
else:
    print('false')