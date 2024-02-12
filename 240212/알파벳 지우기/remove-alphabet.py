a = input()
b = input()

number = []
number1 = []

for i in a:
    if i.isdigit():
        number.append(i)

for j in b:
    if j.isdigit():
        number1.append(j)

number = ''.join(number)
number1 = ''.join(number1)

print(int(number)+ int(number1))