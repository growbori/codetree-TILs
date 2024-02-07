s = input()
n = s[0]
m = s[1]

# print(n, m)
for i in s:
    if i == m:
        s = s.replace(i, n, 100)

print(s)