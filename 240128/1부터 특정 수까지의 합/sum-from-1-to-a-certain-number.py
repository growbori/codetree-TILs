n = int(input())

def div(n):
    total_sum = 0
    for i in range(1, n+1):
        total_sum += i / 10
        i += 1
    return int(total_sum)


total = div(n)

print(total)