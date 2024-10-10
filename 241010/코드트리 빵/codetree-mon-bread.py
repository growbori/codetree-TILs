n, m = list(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(n)]

EMPTY = (-1, -1)
cvs_list = []
for _ in range(m):
    x, y = map(lambda x: int(x)-1, input().split())
    cvs_list.append((x, y))     # 좌표로 받아오기!

people = [EMPTY] * m # 사람들 위치 관리하는 리스트 초기는 격자 밖이므로 -1로 표시

time = 0    # 시간 기록


# 최단거리 결과 기록
step = [[0] * n for _ in range(n)]

# 방문 여부 표시
visited = [[False] * n for _ in range(n)]


def bfs(start_pos):
    # visited, step 모두 초기화
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][i] = 0

    # 초기 위치 넣어주기
    q = []
    q.append(start_pos)
    si, sj = start_pos
    visited[si][sj] = True
    step[si][sj] = 0

    while q:
        ci, cj = q.pop(0)
        for di, dj in  ((-1, 0), (0, -1), (0, 1), (1, 0)):  # 4방향 탐색
            ni, nj = ci + di, cj + dj
            # 범위내, 미방문, 이미 완성된 편의점이 아니면
            if 0<= ni < n and 0 <= nj < n and visited[ni][nj] == 0 and arr[ni][nj] != 2:
                visited[ni][nj] = True
                step[ni][nj] = step[ci][cj] + 1
                q.append((ni, nj))
def simulate():
    for i in range(m):  # 격자에 있는 사람에 한하여 편의점 방향으로 한칸 움직임

        if people[i] == EMPTY or people[i] == cvs_list[i]:  # 격자 밖에 있거나 편의점 도착한 사람이면 패스
            continue
        bfs(cvs_list[i])    # 편의점에서 시작하는 BFS로 진행
        ci, cj = people[i]  # 사람 위치 좌표 받아오기
        min_dist = 10000
        min_x, min_y = -1, -1   # 가장 짧은 거리 초기값 설정해주기
        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and visited[ni][nj] and min_dist > step[ni][nj]:
                min_dist = step[ni][nj]
                min_x, min_y = ni, nj

        people[i] = (min_x, min_y)  # 우선순위가 가장 높은 위치로 한칸 움직임

        # 편의점에 도착한 사람에 한하여 grid 값을 2로 바꿔 이동을 멈추게 한다.
    for i in range(m):
        if people[i] == cvs_list[i] :
            ci, cj = people[i]
            arr[ci][cj] = 2

    # time 에 대해 time <= m을 만족하면 t 번 사람이 베이스 캠프로 간다
    if time > m:
        return

    bfs(cvs_list[time-1])   # 편의점에서 가장 가까운 베이스 캠프로 가기 위해 편의점에서 시작하는 BFS 진행

    min_dist = 10000
    min_x, min_y = -1, -1
    for i in range(n):
        for j in range(n):
            # 방문 가능한 베이스 캠프 중 가장 가까운 위치 찾기
            if visited[i][j] and arr[i][j] == 1 and min_dist > step[i][j]:
                min_dist = step[i][j]
                min_x, min_y = i, j

    people[time-1] = (min_x, min_y)   # 우선순위가 높은 베이스 캠프로 이동
    arr[min_x][min_y] = 2   # 해당 베이스 캠프 앞으로 이동 불가능한 칸임을 표시

def end():
    for i in range(m):
        if people[i] != cvs_list[i]:
            return False
    return True # 전부 편의점에 도착하면 끝임

while True:
    time += 1
    simulate()
    if end():
        break

print(time)