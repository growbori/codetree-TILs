n = int(input())

arr = list(map(int, input().split()))

raa =[]
# 문자 탐색
for i, char in enumerate(arr):
    if char == 2:
        raa.append(i)

print(raa[2]+1)