arr = input().split()
sum_even = 0
sum_odd = 0
n = len(arr)

for i in range(n):
    if i % 2 == 0:
        sum_even += int(arr[i])
    else:
        sum_odd += int(arr[i])
    
if sum_even > sum_odd:
    print(sum_even - sum_odd)
else:
    print(sum_odd - sum_even)