arr = list(map(float, input().split()))

sum_val = 0

for i in range(8):
    sum_val += arr[i]
    div_val = sum_val / 8
print('%0.1f' %div_val)