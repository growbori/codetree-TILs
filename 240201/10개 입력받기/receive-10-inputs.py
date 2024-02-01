new_arr = []

arr = list(map(int, input().split()))

for i in arr:
    if i != 0:
        new_arr.append(i)
    else:
        break
sum_arr = sum(new_arr)
div_arr = sum_arr / len(new_arr)
print(sum_arr, '%0.1f' %div_arr)