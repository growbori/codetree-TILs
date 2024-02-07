sentence = input()
N = len(sentence)
new_sen = sentence[:1] + 'a' + sentence[2:N-2] + 'a' + sentence[N-1:]
print(new_sen)