N, M = map(int, input().split())  # N: 지도의 크기, M: 편의점의 개수 입력받음

# 1로 둘러싸인 지도 생성: N*N의 배열을 1로 둘러싸고 내부는 사용자 입력으로 채움
arr = [[1] * (N + 2)] + [[1] + list(map(int, input().split())) + [1] for _ in range(N)] + [[1] * (N + 2)]

basecamp = set()  # 베이스캠프 위치 저장할 set
for i in range(1, N + 1):  # 지도에서 1(베이스캠프)인 위치를 찾음
    for j in range(1, N + 1):
        if arr[i][j] == 1:  # 베이스캠프는 1로 표시됨
            basecamp.add((i, j))  # 베이스캠프 위치를 set에 저장
            arr[i][j] = 0  # 이동 가능하게 0으로 변경 (베이스캠프가 비워지면 이동 가능)

store = {}  # 편의점 위치 저장할 딕셔너리
for m in range(1, M + 1):  # 각 편의점의 위치를 입력받음
    i, j = map(int, input().split())
    store[m] = (i, j)  # 편의점 번호를 키로 하고 좌표를 값으로 저장

from collections import deque  # 큐를 사용하기 위해 deque 임포트

# 시작 좌표에서 목적지까지 최단 거리로 이동하여 목적지와 같은 거리에 있는 모든 좌표를 찾는 함수
def find(si, sj, dests):
    q = deque()  # BFS를 위한 큐
    v = [[0] * (N + 2) for _ in range(N + 2)]  # 방문 여부를 체크하는 배열
    tlst = []  # 목적지에 도착한 좌표를 저장할 리스트

    q.append((si, sj))  # 시작 좌표를 큐에 추가
    v[si][sj] = 1  # 시작 좌표 방문 표시

    while q:
        nq = deque()  # 현재 단계에서의 새로운 큐
        for ci, cj in q:  # 현재 큐의 좌표들을 확인
            if (ci, cj) in dests:  # 목적지에 도착했으면
                tlst.append((ci, cj))  # 목적지 좌표를 리스트에 추가
            else:
                # 상, 하, 좌, 우 네 방향으로 이동, 미방문이고 벽이 아니면 큐에 추가
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = ci + di, cj + dj
                    if v[ni][nj] == 0 and arr[ni][nj] == 0:  # 미방문, 벽이 아님
                        nq.append((ni, nj))  # 새로운 큐에 추가
                        v[ni][nj] = v[ci][cj] + 1  # 방문 표시

        if len(tlst) > 0:  # 목적지를 찾았으면
            tlst.sort()  # 좌표를 행, 열 기준으로 오름차순 정렬
            return tlst[0]  # 가장 우선순위 높은 좌표 반환
        q = nq  # 다음 단계의 큐로 변경
    return -1  # 목적지에 도착하지 못했을 때 (사실상 이 부분은 실행되지 않음)

def solve():
    q = deque()  # 이동할 사람들의 큐
    time = 1  # 시간 초기화
    arrived = [0] * (M + 1)  # 각 사람이 편의점에 도착한 시간을 기록하는 배열 (도착하지 않으면 0)

    while q or time == 1:  # 처음(시간 1일 때) 또는 이동할 사람이 남아 있을 때까지 반복
        nq = deque()  # 다음 단계에서 이동할 사람들의 큐
        alst = []  # 도착한 사람들의 위치를 저장할 리스트

        # [1] 모두 편의점 방향으로 한 칸씩 이동
        for ci, cj, m in q:  # 현재 위치와 편의점 번호 확인
            if arrived[m] == 0:  # 아직 도착하지 않은 사람만 처리
                # 현재 위치에서 상, 하, 좌, 우로 이동할 수 있는 가장 가까운 좌표 찾기
                ni, nj = find(store[m][0], store[m][1], {(ci - 1, cj), (ci + 1, cj), (ci, cj - 1), (ci, cj + 1)})
                if (ni, nj) == store[m]:  # 편의점에 도착했으면
                    arrived[m] = time  # 도착 시간을 기록
                    alst.append((ni, nj))  # 도착한 좌표를 기록
                else:
                    nq.append((ni, nj, m))  # 아직 도착하지 않은 사람들은 계속 이동

        q = nq  # 다음 단계로 이동할 사람들로 큐 업데이트

        # [2] 편의점에 도착한 사람들의 위치를 이동 불가로 변경
        if len(alst) > 0:
            for ai, aj in alst:
                arr[ai][aj] = 1  # 이동 불가 처리 (다른 사람이 지나가지 못하게 함)

        # [3] 시간 번호에 해당하는 사람이 베이스캠프로 순간이동
        if time <= M:  # 아직 이동하지 않은 사람이 있을 때만
            si, sj = store[time]  # 현재 시간에 해당하는 사람이 이동할 편의점
            ei, ej = find(si, sj, basecamp)  # 베이스캠프에서 가장 가까운 위치 찾기
            basecamp.remove((ei, ej))  # 베이스캠프를 제거 (다른 사람이 들어가지 못하게 함)
            arr[ei][ej] = 1  # 베이스캠프 위치를 이동 불가 처리
            q.append((ei, ej, time))  # 베이스캠프에서 이동 시작

        time += 1  # 시간이 한 단위 증가
    return max(arrived)  # 모든 사람이 도착한 시간 중 가장 큰 값 반환

ans = solve()  # 최종적으로 모든 사람이 도착하는 시간을 계산
print(ans)  # 결과 출력