n = int(input())
home = list(input().split(' '))

result = []
for i in range(len(home)):
    k = 0
    for j in range(len(home)):
        if j != i:
            k += int(home[j]) * abs(j - i)
    result.append(k)
print(min(result))