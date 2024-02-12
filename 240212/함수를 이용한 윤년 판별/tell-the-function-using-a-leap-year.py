def is_onjeonsu(n):
    if n % 4==0 and n % 100 != 0:
        return True
    elif n % 400 == 0:
        return True
    else:
        return False

n = int(input())

if is_onjeonsu(n):
    print('true')
else:
    print('false')