n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        print(f'{i} * {j} = {i*j}', end = '')
        if j < n:
            print(',', end = ' ')
    print()

    #if j < n :
    #    print(',', end = ' ')
    # 적어서 ','넣어주는 것 중요!