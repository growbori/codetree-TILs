n = int(input())
count = 0
for _ in range(n):
    arr = list(map(int, input().split()))
    new_arr = []
    for i in arr:
        new_arr.append(i)

        sum_arr = sum(new_arr)
        div_arr = sum_arr // 4

    # print(div_arr)

    if div_arr >= 60:
        answer = 'pass'
    else:
        answer = 'fail'

    print(answer)
    
    if answer == 'pass':
        count += 1
print(count)