n = int(input())

arr = list(map(int, input().split()))
maxnum = -1
blank = [0] * n

for i in range(n):
    if maxnum < arr[i] and blank[i] == 0:
        maxnum = arr[i]
        blank[i] = 1
    elif maxnum < arr[i] and blank[i] == 1:
        maxnum = -1
    else :
        continue
    


print(maxnum)