'''
비상구(ei, ej) - 11 사람 -1
1. 이동 (동시 이동) => 복사/ 0으로 새로운 arr 적용
사람인 경우 현재위치 ~ 비상구까지 절댓값 거리가 (ni, nj) ~ 비상구 까지 절댓값 거리 보다 크면 상하/좌우 이동
네방향, 범위 내, 벽 아니고, 최단거리면 이동
(ni, nj)가 비상구인 경우, i, j 위치에서 ni, nj narr[ni][nj] -= arr[i][j] cnt += arr[i][j] # 탈출
ans = 0 ans += arr[i][j] (출력할 땐 음수로)
비상구가 아닌 경우, 빈공간이거나 다른 사람이 있는 경우, 합쳐준다!
cnt == 0인 경우 break
비상구와 사람별 최단 거리 (min)값 찾기 - 가로 or 세로
L = 최소값(max(abs(ei - i), abs(ej - j)))
회전 (목적지 기준 !)
사람과 출구 사이의 거리 구할 땐 +1 해주기!
'''


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for _ in range(M):
    i, j = map(lambda x: int(x)-1, input().split())
    arr[i][j] -= 1 # 같은 위치에 여러 명 있을 수 있음

ei, ej = map(lambda x: int(x)-1, input().split())
arr[ei][ej] = - 11

def find_square(arr):
    # 비상구와 모든 사람 간의 가장 짧은 가로 또는 세로 거리 구하기 -> L
    mn = N
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0:     # 사람인 경우
                mn = min(mn, max(abs(ei - i), abs(ej - j)))

    # (0, 0) 부터 순회하면서 길이 L 인 정사각형에 비상구와 사람있는지 체크 -> 리턴
    for si in range(N-mn):
        for sj in range(N-mn):  # 가능한 모든 시작 위치
            if si <= ei <= si + mn and sj <= ej <= sj + mn: # 비상구가 포함된 사각형
                for i in range(si, si + mn + 1):
                    for j in range(sj, sj + mn + 1):
                        if -11 <arr[i][j] < 0:
                            return si, sj, mn + 1


def find_exit(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == - 11:
                return i, j
ans = 0
cnt = M
for _ in range(K):
    # 모든 참가자가 한칸씩 이동 (출구 최단 거리 방향 상/하 우선)
    # 출구에 도착하면 즉시 탈출
    narr = [x[:] for x in arr]
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0: # 사람인 경우
                dist = abs(ei - i) + abs(ej - j)
                # 네 방향 (상하좌우) 범위 내, 벽 아니고 <= 0, ni, nj 거리가 dist 보다 작으면
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] <= 0 and dist > abs(ei-ni) + abs(ej - nj):
                        ans += arr[i][j] # 현재 인원수가 이동하는 것이니 이동거리에 누적
                        narr[i][j] -= arr[i][j]
                        if arr[ni][nj] == - 11: # 비상구라면
                            cnt += arr[i][j]
                        else:   # 일반 빈칸 또는 사람있는 자리
                            narr[ni][nj] += arr[i][j]   # 들어온 인원 추가
                        break
    arr = narr
    if cnt == 0:
        break
    # 미로 회전 (출구와 한명 이상의 참가자를 포함하는 가장 작은 정사각형
    # 시계 방향 90도 : 같은 크기 -> 좌상단행열, 내구도 -1
    si, sj, L = find_square(arr)    # 비상구 + 사람 포함 최소 정사각형

    narr = [x[:] for x in arr]
    for i in range(L):
        for j in range(L):
            narr[si + i][sj + j] = arr[si + L - 1 - j][sj + i]
            if narr[si + i][sj + j] > 0:
                narr[si + i][sj + j] -= 1
    arr = narr
    #회전으로 달라졌으므로 비상구 위치 저장
    ei, ej = find_exit(arr)


print(-ans)
print(ei + 1, ej + 1)