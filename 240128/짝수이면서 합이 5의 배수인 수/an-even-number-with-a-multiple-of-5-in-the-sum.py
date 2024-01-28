n = int(input())

def is_magic_num():
    ten = n // 10
    one = n % 10
    summ = ten + one

    if summ % 5 == 0 and n % 2 == 0:
        print('Yes')
    else:
        print('No')

is_magic_num()