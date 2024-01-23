arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] == 0:
        break
    else:
        if arr[i] % 2 == 1:
            print(arr[i] + 3, end = ' ')
        elif arr[i] % 2 == 0:
            print(arr[i] //2, end = ' ')




    # if arr[i] % 2 == 1:
    #     print(arr[i] + 3, end = ' ')
    # elif arr[i] % 2 == 0:
    #     print(arr[i] //2, end = ' ')
    # elif arr[i] == 0:
    #     break