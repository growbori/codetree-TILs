sentence = ['L''E''B''R''O''S']

idx = -1

# 문자 탐색
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

# 문자가 존재하지 않는 경우
if idx == -1:
    print("None")
else:
    print(idx)