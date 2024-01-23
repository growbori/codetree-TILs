arr = list(map(int, input().split()))
cnt100 = 0
cnt90 = 0
cnt80 = 0
cnt70 = 0
cnt60 = 0
cnt50 = 0
cnt40 = 0
cnt30 = 0
cnt20 = 0
cnt10 = 0
for i in range(len(arr)):
    if arr[i] == 0:
        break
    else:
        if arr[i] //100 == 1:
            cnt100 += 1
        elif arr[i] // 10 == 9:
            cnt90 += 1
        elif arr[i] // 10 == 8:
            cnt80 += 1
        elif arr[i] // 10 == 7:
            cnt70 += 1
        elif arr[i] // 10 == 6:
            cnt60 += 1
        elif arr[i] // 10 == 5:
            cnt50 += 1
        elif arr[i] // 10 == 4:
            cnt40 += 1
        elif arr[i] // 10 == 3:
            cnt30 += 1
        elif arr[i] // 10 == 2:
            cnt20 += 1
        elif arr[i] // 10 == 1:
            cnt10 += 1

print(f'{100} - {cnt100}')
print(f'{90} - {cnt90}')
print(f'{80} - {cnt80}')
print(f'{70} - {cnt70}')
print(f'{60} - {cnt60}')
print(f'{50} - {cnt50}')
print(f'{40} - {cnt40}')
print(f'{30} - {cnt30}')
print(f'{20} - {cnt20}')
print(f'{10} - {cnt10}')