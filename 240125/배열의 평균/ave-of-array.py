arr_2d = []
for _ in range(2):
    arr_1d = list(map(int, input().split()))
    arr_2d.append(arr_1d)

for i in range(len(arr_1d)):
    sumval = sum(arr_2d[0])
    divval = sumval / 4

for i in range(len(arr_2d[1])):
    sumval2 = sum(arr_2d[1])
    divval2 = sumval2 / 4
    
print(divval, divval2)

ver_1 = (arr_2d[0][0] + arr_2d[1][0]) /2
ver_2 = (arr_2d[0][1] + arr_2d[1][1]) /2
ver_3 = (arr_2d[0][2] + arr_2d[1][2]) /2
ver_4 = (arr_2d[0][3] + arr_2d[1][3]) /2

print(ver_1, ver_2, ver_3, ver_4)

sum_val = (divval + divval2)/2
print(sum_val)