arr = list(map(int, input().split()))

cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
cnt6 = 0
cnt7 = 0
cnt8 = 0
cnt9 = 0

for i in range(len(arr)):
    if arr[i] == 0:
        break
    else: 
        if arr[i] // 10 == 1:
            cnt1 += 1
        elif arr[i] // 10 == 2:
            cnt2 += 1
        elif arr[i] // 10 == 3:
            cnt3 += 1
        elif arr[i] // 10 == 4:
            cnt4 += 1
        elif arr[i] // 10 == 5:
            cnt5 += 1
        elif arr[i] // 10 == 6:
            cnt6 += 1
        elif arr[i] // 10 == 7:
            cnt7 += 1
        elif arr[i] // 10 == 8:
            cnt8 += 1
        elif arr[i] // 10 == 9:
            cnt9 += 1

print(f'{1} - {cnt1}')
print(f'{2} - {cnt2}')
print(f'{3} - {cnt3}')
print(f'{4} - {cnt4}')
print(f'{5} - {cnt5}')
print(f'{6} - {cnt6}')
print(f'{7} - {cnt7}')
print(f'{8} - {cnt8}')
print(f'{9} - {cnt9}')