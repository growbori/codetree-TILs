string = input()
n = int(input())

if n > len(string):
    print(string)
else:
    string1 = string[len(string)-n-1:-1]
    string2 = string1[::-1]
    print(string2)