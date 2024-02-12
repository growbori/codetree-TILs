def is_magic_number(n):
    return n % 3 == 0 or str_number(n)

def str_number(n):
    return ('3' in str(n)) or ('6' in str(n)) or ('9' in str(n))


a, b = map(int, input().split())
count = 0
for i in range(a, b+1):
    if is_magic_number(i):
        count += 1

print(count)