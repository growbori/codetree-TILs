txt = list(input())

stack = []
top = -1
for i in txt:
    if len(stack) == 0:
        stack.append(i)

    else:
        if stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

if len(stack) >= 2:
    answer = 'Yes'
else:
    answer = 'No'
print(answer)