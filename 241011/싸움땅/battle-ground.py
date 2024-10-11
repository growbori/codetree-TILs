'''
1번 플레이어부터 순서대로 진행 진행 방향대로 한칸 이동, 만약 격자를 벗어나는 경우엔 정 반대방향으로 방향 바꾸어 1 이동
이동한 칸에 플레이어가 없다면, 총 획득 이미 총이 있는 경우에는 공격력이 더 쎈 총을 획득하고 나머지 총은 격자에 둠
-> 손에 들 수 있는 총은 결국 하나다! units로 입력 받자!
units = {[1: 가진 공격력, 0 -> 총 주울 경우 그 공격력, 승리 포인트]}
같은 칸에 만날 경우 fight. 초기 능력치와 가진 공격력의 합이 더 높은 플레이어 승리
수치가 같을 경우에는 초기 능력치가 높은 플레이어 승리
이긴 플레이어는 (초기 능력치 + 공격력의 합) 차이 만큼 포인트 획득 예시의 경우 6 - 5
진 플레이어는 본인이 가진 총을 격자에 내려놓고, 원래 가던대로 한칸 이동한다 -> 이동하려는 칸에 플ㄹ이어가 있거나 격자 밖인 경우 90도 회전하여 빈칸일때 이동 visited 배열 써야 함!
이긴 플레이어는 승리한 칸에 떨어진 총과 원래 들고있던 총 중 가장 공격력이 높은 총 획득 나머지 버림 -> 결국 든 총은 하나!
K 라운드동안 게임 진행하면서 플레이어가 획득한 포인트를 출력 units[i][4] 를 하나의 리스트에 받고 그 결과를 출력하는 것

'''
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
units = {}
visited = [[0] * N for _ in range(N)]   # 격자 칸에 사람 있을 경우 다른 칸으로 이동해야 하니까 체크!
for m in range(1, M+1):
    i, j, d, s = map(int, input().split())
    units[m] = [i-1, j-1, d, s, 0, 0] # 뒤에 0, 0은 총의 공격력과 승리 포인트
    visited[i-1][j-1] = m   # 플레이어 정보 작성
ans = []    # 획득 포인트 리스트로 받아내서 정리하기
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]  # 상/우/하/좌 순서로 이동

def fight(arr, visited, ni, nj, units):
    x = units[m][3]     # player1 공격력
    y = units[m][4]     #player1총의 공격력
    k = visited[ni][nj] # player2의 번호
    l = units[k][3]
    z = units[k][4]
    if x + y > l + z:
        units[m][5] = (x + y) - (l + z)
        winner = m
        loser = k
    else:
        units[k][5] = (l + z) - (x + y)
        winner = k
        loser = m
    fight_loser(arr, visited, units, loser)
    fight_winner(arr, visited, units, winner)

def fight_winner(arr, visited, units, winner):
    x = winner
    ci, cj, dr, gun = units[x][0], units[x][1], units[x][2], units[x][4]
    visited[ci][cj] = x
    for di, dj in ((-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1), (1, 0), (1, 1), (1, -1)):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > gun:
            units[x][4] = arr[ni][nj]
            arr[ni][nj] = gun

def fight_loser(arr, visited, units, loser):
    x = loser
    units[x][4] = 0 # 본인이 가지고 있는 총 내려놓기
    ci, cj, dr = units[x][0],units[x][1], units[x][2]
    ni, nj  = ci + di[dr], cj + dj[dr]
    if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
        units[x][0], units[x][1] = ni, nj   # 다음칸 이동
        visited[ni][nj] = x
        if arr[ni][nj] != 0:    # 총이 있으면
            gun = arr[ni][nj]
            if gun > units[x][4]:
                units[x][4] = gun
                arr[ni][nj] = 0
    elif (ni == 0 or nj == 0 or ni == N-1 or nj == N-1) or visited[ni][nj] == 1: # 격자 밖인 경우 90도 회전
        dr = (dr+1) % 4
        ni, nj = ci + di[dr], cj + dj[dr]
        visited[ci][cj] = 0
        visited[ni][nj] = x
        units[x][0], units[x][1], units[x][2] = ni, nj, dr
        if arr[ni][nj] != 0:  # 총이 있으면
            gun = unit[x][4]
            if gun > units[x][4]:
                units[x][4] = 0
                arr[ni][nj] = gun
            else:
                pass




# 플레이어 이동
for _ in range(K):  # 총 K 라운드
    for m in range(1, M+1):  # 플레이어 전부 진행 예정

        ci, cj, dr = units[m][0], units[m][1], units[m][2]
        ni, nj = ci + di[dr], cj + dj[dr]
        # 미방문, 사람 없음, 범위 내 이면 그냥 감
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            visited[ci][cj] = 0 # 원래 있던 자리 0으로 만들기
            visited[ni][nj] = m #새로간 칸에 1이라고 하기
            units[m][0], units[m][1] = ni, nj
            # 더 큰 총 챙기기
            if arr[ni][nj] > units[m][4]:   # 가진 총이 칸에 있는 총보다 작으면
                gun = arr[ni][nj]
                arr[ni][nj] = units[m][4]   # 총 바꿔주기
                units[m][4] = gun
            else:
                continue    # 총 바꾸지 않고 지나가기
        # 맨 끝 방향이면 방향 바꿔서 진행하기
        elif ni == 0 or nj == 0 or ni == N-1 or nj == N-1:
            visited[ci][cj] = 0
            dr = (dr+2) % 4
            ni, nj = ci + di[dr], cj + dj[dr]
            units[m][0], units[m][1], units[m][3] = ni, nj, dr
            if visited[ni][nj] == 0:
                visited[ni][nj] = m
                # 더 큰 총 챙기기
                if arr[ni][nj] > units[m][4]:   # 가진 총이 칸에 있는 총보다 작으면
                    gun = arr[ni][nj]
                    arr[ni][nj] = units[m][4]   # 총 바꿔주기
                    units[m][4] = gun
                else:
                    continue    # 총 바꾸지 않고 지나가기
        # 사람 있으면 싸움! fight(함수 쓰기!)
        elif visited[ni][nj] != 0:
            visited[ci][cj] = 0
            units[m][0], units[m][1] = ni, nj
            fight(arr, visited, ni, nj, units)
            # 게임이 끝난 후 gameover(함수 쓰기!)


# 획득 포인트 정리하기 (리스트 형태로 받기
check = list(units.values())
for i in range(len(check)):
    ans.append(check[i][5])

print(*ans)