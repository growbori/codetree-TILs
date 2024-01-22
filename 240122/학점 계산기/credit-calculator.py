n = int(input())
sum_val = 0

arr = list(map(float, input().split()))
a = len(arr)
for j in range(a):
    sum_val += arr[j]
        
    div_val = sum_val / n
print('%0.1f' %div_val)

if div_val >= 4.0:
    print('Perfect')
elif div_val >= 3.0 :
    print('Good')
else :
    print('Poor')