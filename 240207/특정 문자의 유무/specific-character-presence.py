sentence = input()
length = len(sentence) 
exists = 'No'
exists2 = 'No'
for i in range(length-1):
    if sentence[i:i+2] == 'ee':
        exists = 'Yes'

for i in range(length-1):
    if sentence[i:i+2] == 'ab':
        exists2 = 'Yes'

print(exists, exists2)