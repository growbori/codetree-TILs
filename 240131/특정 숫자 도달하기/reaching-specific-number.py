arr = list(map(int, input().split()))

arr_list = []
for i in range(len(arr)):
    arr_list.append(arr[i])
    if arr[i] >= 250:
        break
arr_list.pop() 
sum_arr = sum(arr_list)
div_arr = sum_arr / len(arr_list)
print(sum_arr, '%0.1f' %div_arr)