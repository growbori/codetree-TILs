n = int(input())
for _ in range(n):
    element = int(input())

    if element % 2 != 0 and element % 3 == 0:
        print(element)
    else:
        continue