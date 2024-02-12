count = 0
answer = []
for i in range(200):
    string = input()
    if string == '0':
        break
    
    else:
        count +=1
        if i % 2 == 0:
            answer.append(string)

print(count)

for i in answer:
    print(i)