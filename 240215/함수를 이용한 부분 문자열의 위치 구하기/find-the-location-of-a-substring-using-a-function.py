full_txt = input()
txt = input()

c = len(txt)
for i in range(len(full_txt)):
    if full_txt[i:i+c] == txt:
        answer = i
        break
    else:
        answer = -1

print(answer)