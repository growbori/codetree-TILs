N = int(input())  # 격자의 크기
students = []
for _ in range(N * N):
    n1, n2, n3, n4, n5 = map(int, input().split())
    students.append([n1, n2, n3, n4, n5])

# 격자
arr = [[0] * N for _ in range(N)]

# 방향 (상, 하, 좌, 우)
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 학생 배치 함수
def find_seat(student_num, friends):
    max_friends = -1
    max_empty = -1
    selected_i = selected_j = -1
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:  # 빈 칸일 때만 고려
                friend_count = 0
                empty_count = 0
                
                # 인접한 4칸을 확인
                for d in range(4):
                    ni, nj = i + di[d], j + dj[d]
                    if 0 <= ni < N and 0 <= nj < N:
                        if arr[ni][nj] in friends:
                            friend_count += 1
                        elif arr[ni][nj] == 0:
                            empty_count += 1
                
                # 조건에 따라 좌석 선택
                if (friend_count > max_friends or
                    (friend_count == max_friends and empty_count > max_empty) or
                    (friend_count == max_friends and empty_count == max_empty and i < selected_i) or
                    (friend_count == max_friends and empty_count == max_empty and i == selected_i and j < selected_j)):
                    max_friends = friend_count
                    max_empty = empty_count
                    selected_i, selected_j = i, j
    
    # 해당 위치에 학생 배치
    arr[selected_i][selected_j] = student_num

# 각 학생을 차례로 배치
for student in students:
    find_seat(student[0], student[1:])

# 점수 계산
def calculate_score():
    score = 0
    for i in range(N):
        for j in range(N):
            student_num = arr[i][j]
            for student in students:
                if student[0] == student_num:
                    friends = student[1:]
                    break

            # 인접한 친구 수 세기
            friend_count = 0
            for d in range(4):
                ni, nj = i + di[d], j + dj[d]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] in friends:
                    friend_count += 1

            # 점수 부여
            if friend_count == 1:
                score += 1
            elif friend_count == 2:
                score += 10
            elif friend_count == 3:
                score += 100
            elif friend_count == 4:
                score += 1000
    
    return score

# 최종 점수 출력
print(calculate_score())