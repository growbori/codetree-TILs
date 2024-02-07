A = input()
B = input()
N = len(B)
count = 0
for i in range(len(A)):
    if A[i: i+N] == B:
        count += 1

print(count)