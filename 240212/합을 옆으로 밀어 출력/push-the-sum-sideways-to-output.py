n = input()
sum = 0
for _ in range(int(n)):
    arr = input()
    sum += int(arr)

sum = str(sum)
# print(type(sum))
print(sum[1:] + sum[0])