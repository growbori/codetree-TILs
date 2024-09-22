a, b = map(int, input().split())
nums = list(map(int, input().split()))
for tc in range(a) :
    check = list(map(int, input().split()))
    if check[0] == 1:
        print(nums[check[1]-1])
    elif check[0] == 2:
        for i in range(a):
            if nums[i] == check[1] :
                print(i+1)
                break
        else :
            print(0)
    else :
        for i in range(check[1]-1, check[2]):
            print(nums[i], end = ' ')
        print()