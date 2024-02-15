def abschange():
    new_arr = []
    for i in arr:
        if i < 0:
            new_arr.append(abs(i))
        else:
            new_arr.append(i)

    return new_arr

N = int(input())

arr = list(map(int, input().split()))

print(*abschange())