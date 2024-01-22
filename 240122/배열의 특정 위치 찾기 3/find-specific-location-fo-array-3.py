n = list(map(int, input().split()))

for i in range(len(n)):
    if n[i] == 0:
        sum_val = n[i-3] + n[i-2] + n[i-1]
        break
print(sum_val)