def is_onjeonsu(n):
    if n % 4 == 0 and n % 100 == 0:
        return False

    return True

n = int(input())

if is_onjeonsu(n):
    print('true')
else:
    print('false')