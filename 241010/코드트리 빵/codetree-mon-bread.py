N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
empty = (-1, -1)
cvs = []
for _ in range(M):
    i, j = map(lambda x: int(x) - 1, input().split())
    cvs.append((i, j))
people = [empty] * M
time = 0
step = [[0] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]  # False로 초기화

def bfs(start_pos):
    # step과 visited 배열을 명확하게 초기화
    for i in range(N):
        for j in range(N):
            step[i][j] = 0
            visited[i][j] = False

    # BFS 초기 설정
    q = [start_pos]
    si, sj = start_pos
    visited[si][sj] = True
    step[si][sj] = 0

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):  # 4방향 탐색
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] != 2:
                visited[ni][nj] = True
                step[ni][nj] = step[ci][cj] + 1
                q.append((ni, nj))

def simulate():
    for i in range(M):
        if people[i] == empty or people[i] == cvs[i]:  # 격자 밖에 있거나 편의점에 도착한 경우
            continue

        # 편의점 기준 BFS 실행
        bfs(cvs[i])
        ci, cj = people[i]
        min_dist = float('inf')
        min_i, min_j = -1, -1  # 가장 가까운 좌표를 찾기 위한 초기값

        # 4방향 탐색하며 가장 가까운 거리 찾기
        for di, dj in ((-1, 0), (0, -1), (0, 1), (1, 0)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] and step[ni][nj] < min_dist:
                min_dist = step[ni][nj]
                min_i, min_j = ni, nj

        if min_i != -1 and min_j != -1:
            people[i] = (min_i, min_j)  # 우선순위가 가장 높은 곳으로 이동

    # 도착한 사람의 위치를 2로 바꿔서 더 이상 이동하지 않도록 처리
    for i in range(M):
        if people[i] == cvs[i]:
            ci, cj = people[i]
            arr[ci][cj] = 2

    # time이 M보다 작은 경우, 새로운 사람 베이스 캠프 이동
    if time <= M:
        bfs(cvs[time - 1])

        min_dist = float('inf')
        min_i, min_j = -1, -1

        # 가장 가까운 베이스 캠프 찾기
        for i in range(N):
            for j in range(N):
                if visited[i][j] and arr[i][j] == 1 and step[i][j] < min_dist:
                    min_dist = step[i][j]
                    min_i, min_j = i, j

        # 해당 베이스 캠프로 이동
        if min_i != -1 and min_j != -1:
            people[time - 1] = (min_i, min_j)
            arr[min_i][min_j] = 2  # 해당 위치를 2로 바꿔서 다른 사람이 못 오도록 처리

# 종료 조건
def end():
    for i in range(M):
        if people[i] != cvs[i]:  # 한 사람이라도 편의점에 도착하지 않으면 종료하지 않음
            return False
    return True  # 모든 사람이 도착한 경우 종료

# 시뮬레이션 반복
while True:
    time += 1
    simulate()
    if end():
        break

print(time)