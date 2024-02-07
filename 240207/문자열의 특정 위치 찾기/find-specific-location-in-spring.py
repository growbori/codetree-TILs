sentence, b = input().split()

if b in sentence:
    print(sentence.index(b))
else:
    print('No')