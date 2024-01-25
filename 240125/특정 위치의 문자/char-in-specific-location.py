sentence = 'LEBROS'

idx = -1

for i in range(len(sentence)):
    if sentence[i] == 'L':
        idx = i
    elif sentence[i] == 'E':
        idx = i
    elif sentence[i] == 'B':
        idx = i
    elif sentence[i] == 'R':
        idx = i
    elif sentence[i] == 'O':
        idx = i
    elif sentence[i] == 'S':
        idx = i
if idx == -1:
    print('None')
else:
    print(i)