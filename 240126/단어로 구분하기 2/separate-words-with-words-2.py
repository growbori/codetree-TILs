# 공백 단위로 문자열을 입력받습니다.
string = input().split()

# 문자열을 출력합니다.
for i in range(len(string)):
    if i % 2 == 0:
	    print(string[i])