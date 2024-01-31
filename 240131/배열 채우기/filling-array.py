arr = list(map(int, input().split()))
n = len(arr)

for i in range(n):
    if arr[i] == 0:
        arr.pop()
        break
print(*arr[::-1])


# [83, 5, 13, 1, 3]이렇게 나타난 결괏 값을 83 5 13 1 3 이렇게 바꿔주고 싶으면 
# print(출력하고자 하는 값)의 출력하고자 하는 값 앞에 *를 붙여주면 된다.
# print(*출력하고자 하는 값)