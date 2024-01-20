n = int(input())
if n <= 7:
    if n % 2 ==1:
        answer = 31
    elif n == 2:
        answer = 28
    else:
        answer = 30
else:
    if n % 2 != 0:
        answer = 30
    elif n % 2 == 0:
        answer = 31


print(answer)