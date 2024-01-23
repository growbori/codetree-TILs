a, b = map(int, input().split())

arr = [a, b]
for i in range(2, 10):
    arr.append(arr[i-1] + 2*(arr[i-2]))

# print(arr)

sentence = ' '.join(map(str, arr))
print(sentence)

# 리스트를 문자열로 변환해서 결합하고자 할 땐, .join()함수를 사용하면 된다.

# 또한 만약 

# sentence = ' '.join(arr) 그냥 이렇게 작성해서

# TypeError: sequence item 0: expected str, int found 가 발생할 경우

# sentence = ' '.join(map(str, arr)) 이렇게 문장에 map을 추가하면 된다.