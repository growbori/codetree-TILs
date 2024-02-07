sentence = input()
new_list = []
for i in sentence:
    if 97 <= ord(i) <= 122:
        new_list.append(i)
    if 65 <= ord(i) <= 90:
        new_list.append(i)
new_list = ''.join(new_list)
print(new_list.upper())
    



# ord(A) = 65 ord (Z) = 90 ord(a) = 97 ord(z) = 122