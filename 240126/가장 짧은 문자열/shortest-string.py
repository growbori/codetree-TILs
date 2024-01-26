str_1 = input()
str_2 = input()
str_3 = input()

if len(str_1) < len(str_2) < len(str_3):
    print(len(str_3) - len(str_1))

elif len(str_1) < len(str_3) < len(str_2):
    print(len(str_2) - len(str_1))

elif len(str_2) < len(str_1) < len(str_3):
    print(len(str_3) - len(str_2))

elif len(str_2) < len(str_3) < len(str_1):
    print(len(str_1) - len(str_2))

elif len(str_3) < len(str_1) < len(str_2):
    print(len(str_2) - len(str_3))

elif len(str_3) < len(str_2) < len(str_1):
    print(len(str_1) - len(str_3))