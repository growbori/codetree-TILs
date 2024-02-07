# ord(A) = 65 ord (Z) = 90 ord(a) = 97 ord(z) = 122

email = input()
low_email = email.lower()
new_email = []
for i in low_email:
    if 97 <= ord(i) <= 122:
        new_email.append(i)
    if i == '0':
        new_email.append(i)
    if i == '1':
        new_email.append(i)
    if i == '2':
        new_email.append(i)
    if i == '3':
        new_email.append(i)
    if i == '4':
        new_email.append(i)
    if i == '5':
        new_email.append(i)
    if i == '6':
        new_email.append(i)
    if i == '7':
        new_email.append(i)
    if i == '8':
        new_email.append(i)
    if i == '9':
        new_email.append(i)

print(''.join(new_email))