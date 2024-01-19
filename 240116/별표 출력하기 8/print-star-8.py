n = int(input())

for i in range(n):
    if i % 2 != 0:
        for j in range(i + 1):
            print('*', end = ' ')
        print()
    else:
        print('*')

# print()를 어디에 적느냐에 따라 출력 값이 변할 수 있다!