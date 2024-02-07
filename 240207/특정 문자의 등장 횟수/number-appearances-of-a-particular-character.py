sentence = input()
count = 0
count2 = 0
for i in range(len(sentence)-1):
    if sentence[i: i+2] == 'ee':
        count += 1
    if sentence[i:i+2] =='eb':
        count2 += 1
print(count, count2)