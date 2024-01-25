n = 4
arr2 = []
for i in range(4):
    arr = list(map(int, input().split()))
    arr2.append(arr)


summ = arr2[0][0] + arr2[1][0] + arr2[1][1] + arr2[2][0] + arr2[2][1] +arr2[2][2] +  arr2[3][0] + arr2[3][1] + arr2[3][2] + arr2[3][3]

print(summ)