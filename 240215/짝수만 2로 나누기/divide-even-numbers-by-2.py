def div2():

    for i in arr:
        if i % 2 == 0:
            i = i // 2
        else:
            i = i
        
        print(i, end = ' ')

N = int(input())

arr = list(map(int, input().split()))

div2()