N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
units = {}
visited = [[0] * N for _ in range(N)]  # 격자 칸에 사람 있을 경우 체크
for m in range(1, M + 1):
    i, j, d, s = map(int, input().split())
    units[m] = [i - 1, j - 1, d, s, 0, 0]  # i, j 위치 / d 방향 / s 초기 공격력 / 0 총 공격력 / 0 승리 포인트
    visited[i - 1][j - 1] = m  # 플레이어 정보 작성
ans = []  # 획득 포인트 리스트로 받아내서 정리하기
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]  # 상/우/하/좌 순서로 이동


# 패배한 플레이어가 이동하는 함수
def fight_loser(arr, visited, units, loser):
    ci, cj, dr = units[loser][0], units[loser][1], units[loser][2]
    arr[ci][cj] = units[loser][4]  # 총을 격자에 내려놓음
    units[loser][4] = 0  # 총을 버림

    ni, nj = ci + di[dr], cj + dj[dr]

    # 이동하려는 칸이 격자 밖이거나 사람이 있으면 90도 회전하여 빈칸을 찾아 이동
    while not (0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0):
        dr = (dr + 1) % 4  # 90도 회전
        ni, nj = ci + di[dr], cj + dj[dr]

    # 이동한 칸이 빈칸이므로 이동
    visited[ci][cj] = 0
    visited[ni][nj] = loser
    units[loser][0], units[loser][1], units[loser][2] = ni, nj, dr

    # 이동한 칸에 총이 있으면 총을 획득
    if arr[ni][nj] != 0:
        gun = arr[ni][nj]
        units[loser][4] = gun
        arr[ni][nj] = 0


# 승리한 플레이어가 처리하는 함수
def fight_winner(arr, visited, units, winner):
    ci, cj = units[winner][0], units[winner][1]
    gun = units[winner][4]  # 승리한 플레이어의 총
    # 승리한 칸에서 더 큰 총이 있으면 교체
    if arr[ci][cj] > gun:
        units[winner][4], arr[ci][cj] = arr[ci][cj], gun


# 두 플레이어가 싸우는 함수
def fight(arr, visited, ni, nj, units, m):
    m1 = visited[ni][nj]  # 현재 칸에 있는 player1의 번호
    m2 = m  # 이동해온 player2

    power1 = units[m1][3] + units[m1][4]  # player1의 총합 공격력
    power2 = units[m2][3] + units[m2][4]  # player2의 총합 공격력

    # 공격력이 다르면 더 큰 공격력을 가진 플레이어가 승리
    if power1 > power2:
        winner, loser = m1, m2
        units[winner][5] += power1 - power2  # 승리 포인트 추가
    elif power2 > power1:
        winner, loser = m2, m1
        units[winner][5] += power2 - power1  # 승리 포인트 추가
    # 공격력이 같으면 초기 능력치로 비교
    else:
        if units[m1][3] > units[m2][3]:
            winner, loser = m1, m2
        else:
            winner, loser = m2, m1
        units[winner][5] += abs(units[winner][3] - units[loser][3])  # 초기 능력치 차이만큼 포인트 추가

    # 패배자와 승리자 각각 처리
    fight_loser(arr, visited, units, loser)  # 패배자 이동
    fight_winner(arr, visited, units, winner)  # 승리자는 총 교체


# K번의 라운드 동안 게임 진행
for _ in range(K):
    for m in range(1, M + 1):
        ci, cj, dr = units[m][0], units[m][1], units[m][2]
        ni, nj = ci + di[dr], cj + dj[dr]

        # 격자를 벗어나면 방향 반대로 변경
        if not (0 <= ni < N and 0 <= nj < N):
            dr = (dr + 2) % 4
            ni, nj = ci + di[dr], cj + dj[dr]

        # 이동한 칸이 빈칸이면 이동
        if visited[ni][nj] == 0:
            visited[ci][cj] = 0
            visited[ni][nj] = m
            units[m][0], units[m][1], units[m][2] = ni, nj, dr
            # 더 큰 총이 있으면 총 획득
            if arr[ni][nj] > units[m][4]:
                units[m][4], arr[ni][nj] = arr[ni][nj], units[m][4]

        # 이동한 칸에 다른 플레이어가 있으면 싸움
        else:
            fight(arr, visited, ni, nj, units, m)

# 각 플레이어의 포인트 출력
ans = [units[i][5] for i in range(1, M + 1)]
print(*ans)