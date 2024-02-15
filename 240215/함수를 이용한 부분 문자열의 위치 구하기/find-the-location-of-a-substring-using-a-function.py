def findword():
    global full_txt
    global txt
    global c
    for i in range(len(full_txt)):
        if full_txt[i:i+c] == txt:
            answer = i
            break
        else:
            answer = -1

    return answer

full_txt = input()
txt = input()
c = len(txt)

print(findword())