arr = list(map(int, input().split()))
n = len(arr)
sum_val = 0
sum_val_2 = 0
for i in range(1, n, 2):
    sum_val += arr[i]

for i in range(2, n, 3):
    sum_val_2 += arr[i]
    mol = n // 3
    div_mal = sum_val_2 / mol
print(sum_val, '%0.1f' % div_mal)