string = input()
n = int(input())

if n > len(string):
    print(string)
else:
    string1 = string[len(string)-n:]
    string2 = string1[::-1]
    print(string2)