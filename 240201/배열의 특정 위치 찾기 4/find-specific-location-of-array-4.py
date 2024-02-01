arr = list(map(int, input().split()))

new_arr = []
for i in arr:
    if i != 0:
        if i % 2 == 0:
            new_arr.append(i)
    else:
        break

sum_arr = sum(new_arr)
l = len(new_arr)

print(l, sum_arr)