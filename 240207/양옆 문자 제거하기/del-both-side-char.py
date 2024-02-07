sentence = input()
n = len(sentence)
new_s = sentence[:1] + sentence[2:n-2] + sentence[n-1:] 

print(new_s)