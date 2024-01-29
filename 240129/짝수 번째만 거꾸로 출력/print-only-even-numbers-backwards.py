n = input()
nlist = []
for i in range(len(n)):
    if i % 2 != 0:
        nlist.append(n[i])
nlist2 = nlist[::-1]

new_str = ''.join(nlist2)

print(new_str)