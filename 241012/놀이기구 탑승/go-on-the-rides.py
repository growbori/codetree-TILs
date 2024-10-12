N = int(input())
student = []
for _ in range(N*N):
    n1, n2, n3, n4, n5 = map(int, input().split())
    student.append([n1, n2, n3, n4, n5])

arr = [[0] * N for _ in range(N)]
arr[N // 2][N//2] = student[0][0]


for m in range(1, N*N):
    student_num = student[m][0]
    check = student[m][1:]
    if m == (N* N-1) :
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 0:
                    arr[i][j] = student_num
                    break

    else:
        narr = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 0:
                    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < N and 0 <= nj < N and (arr[ni][nj] in check):
                            narr[i][j] += 1


        mx_cnt = 0
        loc_list = []
        for i in range(N):
            for j in range(N):
                if narr[i][j] > mx_cnt:
                    loc_list.append((i, j))

        for i in range(len(loc_list)):
            mx_x = loc_list[i][0]
            mx_y = loc_list[i][1]
            if arr[mx_x][mx_y] == 0:
                arr[mx_x][mx_y] = student_num
                break
            else:
                i += 1




di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# 결과표에서 구하기
ans = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        for k in range(N*N):
            if arr[i][j] == student[k][0]:
                for dr in range(4):
                    ni, nj = i + di[dr], j + dj[dr]
                    if 0 <= ni < N and 0 <= nj < N and (arr[ni][nj] in student[k]):
                        cnt += 1

        if cnt == 1:
            ans += 1
        elif cnt == 2:
            ans += 10
        elif cnt == 3:
            ans += 100
        elif cnt == 4:
            ans += 1000

print(ans)