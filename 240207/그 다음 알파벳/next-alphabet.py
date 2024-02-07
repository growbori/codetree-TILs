a = input() # z = 122 a= 97

if ord(a) == 122:
    b = ord(a) - 25
else:
    for i in range(97, 122):
        b = ord(a)+1
print(chr(b))
# print(chr(b))
# print(ord(a))
# b = ord(a)
# print(chr(b))