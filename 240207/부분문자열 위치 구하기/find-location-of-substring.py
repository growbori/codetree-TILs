sentence = input()
word = input()
n = len(word)
answer = -1
for i in range(len(sentence)-1):
    if sentence[i:i+n] == word:
        answer = sentence.index(word[0])
        

print(answer)