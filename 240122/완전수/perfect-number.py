a, b = input().split()
sum_j = 0
cnt = 0
for i in range(int(a),int(b)+1):
    for j in range(1, i + 1):
        if i % j == 0:
            sum_j += j
            if sum_j == i:
                cnt += 1
print(cnt)