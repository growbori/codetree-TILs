a, o, c = input().split()

def cal():
    if o == '+':
        print(a, o, c, '=', int(a)+int(c))
    elif o == '-':
        print(a, o, c, '=', int(a)-int(c))
    elif o == '*':
        print(a, o, c, '=', int(a)*int(c))
    elif o == '/':
        print(a, o, c, '=', int(a)//int(c))
    else:
        print('False')
    return

cal()