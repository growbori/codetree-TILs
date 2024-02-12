a = input()
b = input()

count = 0
for i in range(len(a)):
    c = a[i:] + a[:i]
    if c == b:
        count += i
    else:
        count += 0

if count >0:
    answer = count
else:
    answer = -1

print(answer)