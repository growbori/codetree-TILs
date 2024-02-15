def is_palindrome(A):
    for i in range(len(A)):
        if A[i] == A[len(A) - i-1]:
            answer = 'Yes'
        else:
            answer = 'No'

    print(answer)


A = input()

is_palindrome(A)

# A = input()

# for i in range(len(A)):
#     if A[i] == A[len(A) - i-1]:
#         answer = 'Yes'
#     else:
#         answer = 'No'

# print(answer)