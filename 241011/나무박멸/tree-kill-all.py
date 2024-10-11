'''
나무가 있는 칸의 수 만큼 나무가 성장 -> 총 격자에 몇개의 나무가 있는지 세야함
기존의 나무들은 인접한 4개의 칸 중 벽, 다른 나무, 제초제 모두 없는 칸에서 번식 진행
각 칸의 나무 수 // 번식이 가능한 칸의 개수만큼 번식 모든 과정 동시에
가장 나무가 많이 박멸되는 칸에 제초제 뿌림(4개의 대각선 방향으로 K 만큼 전파) c년 만큼 제초제 있다가 c+1될때 사라짐
박멸시키는 나무의 수가 동일한 경우에는 행이 작은 순서, 열이 작은 순서로 제초제 사용
박멸 진행 년수 m, 제초제 확산 범위 k, 제초제가 남아있는 년수 c
벽 -1
'''

N, M, K, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

killer = [[0] * N for _ in range(N)]    # 제초제 뿌리고 C동안 영향 받는 것을 나타낼 판
ans = 0  # 박멸한 나무의 수
for _ in range(M):
    # C 1씩 감소시켜 주기
    for i in range(N):
        for j in range(N):
            if killer[i][j] > 0:
                killer[i][j] -= 1
    # 1. 나무의 성장
    narr = [[0] * N for _ in range(N)]  # 성장 정도를 저장할 리스트
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:   # 나무가 있는 칸이고 주위에 도 나무가 있으면
                for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ni, nj = i + di, j + dj
                    # 범위 내이고 나무가 있으면
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > 0:
                        narr[i][j] += 1
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] + narr[i][j]

    # 2. 나무의 번식
    garr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ni, nj = i + di, j + dj
                    # 범위 내이고, 벽, 다른 나무, 제초제가 없으면 성장
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0 and killer[ni][nj] == 0:
                        garr[i][j] += 1

    karr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ni, nj = i + di, j + dj
                    # 범위 내이고, 벽, 다른 나무, 제초제가 없으면 성장
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0 and killer[ni][nj] == 0:
                        if (arr[i][j] // garr[i][j]) > 0:
                            karr[ni][nj] += (arr[i][j] // garr[i][j])
                        else:
                            continue
    # 번식 결과 저장
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j] + karr[i][j]

    # 제초제 뿌리기
    harr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 0:
                harr[i][j] += arr[i][j]
                for k in range(1, K + 1):
                    for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                        ni, nj = i + di * k, j + dj * k
                        if 0 <= ni < N and 0 <= nj < N:
                            if arr[ni][nj] > 0 and killer[ni][nj] == 0:
                                harr[i][j] += arr[ni][nj]
                            elif arr[ni][nj] == -1:
                                break

    max_kill = 0
    mx_kill_loc = (-1, -1)
    for i in range(N):
        for j in range(N):
            if harr[i][j] > max_kill:
                max_kill = harr[i][j]
                mx_kill_loc = (i, j)


    ci, cj = mx_kill_loc
    ans += arr[ci][cj]
    arr[ci][cj] = 0     # 제초제 영향 표시
    for k in range(N):
        for di, dj in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
                ni, nj = ci + di * k, cj + dj * k
                if 0 <= ni < N and 0 <= nj < N:
                    ans += arr[ni][nj]
                    arr[ni][nj] = 0
                    killer[ni][nj] += (C + 1)



print(ans)