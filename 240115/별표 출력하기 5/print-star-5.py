n = int(input())

for i in range(n):
    for j in range((n-i)):
        print('*'*(n-i), end = ' ')
    print()

# for i in range(n):
#     for j in range((n-i)*(n-i)):
#         print('*', end = ' ')
#     print()
# 아래거랑 차이점이 뭘지 생각해보기