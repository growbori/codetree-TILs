word = input()
ans = []
count = 0
for i in range(len(word)-1):
    if (word[i] == word[i+1]) and (i != len(word)- 2):
        check = word[i]
        count += 1

    elif  word[i] !=word[i+1] :
        ans.append(check)
        check = word[i+1]
        ans.append(count+1)
        count = 0
    else :
        check = word[i]
        count += 1
        ans.append(check)
        ans.append(count +1)

total = 0
for i in range(len(ans)):
    if len(str(ans[i])) == 1:
        total += 1;
    elif len(str(ans[i])) == 2:
        total += 2;
    else:
        total += 3;

print(total)

for i in range(len(ans)):
    print(ans[i], end = '')