word = input()
ans = []
count = 1  # 반복되는 문자를 세기 위한 카운트

for i in range(len(word) - 1):
    if word[i] == word[i + 1]:
        count += 1
    else:
        ans.append(word[i])
        ans.append(count)
        count = 1  # 새로운 문자가 시작되므로 카운트를 1로 초기화

# 마지막 문자와 그 개수를 처리
ans.append(word[-1])
ans.append(count)

# 압축된 결과의 길이 계산
total = 0
for i in range(len(ans)):
    total += len(str(ans[i]))

print(total)

# 압축된 문자열 출력
for i in range(len(ans)):
    print(ans[i], end='')