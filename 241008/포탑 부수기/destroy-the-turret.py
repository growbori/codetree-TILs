N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def find_attacker(arr, x, y, z, k):
    q= []
    q.append((x, y, [(x, y)]))
    v= [[0] * M for _ in range(N)]
    v[x][y] = 1
    while q:
        ci, cj, path = q.pop(0)
        if ci == z and cj == k:
            return path
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):   # 우/하/좌/상 순으로 경로 탐색
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and arr[ni][nj] > 0:
                q.append((ni, nj, path + [(ni, nj)]))
                v[ni][nj] = 1
    return None # path가 없는 경우 None을 적기!


for _ in range(K):# K 번 반복
    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                cnt += 1
    if cnt == 1:    # 0 이 아닌 포탑의 갯수 세기 -> 1이면 종료
        break
    min_power = 5001
    max_power = 0
    for j in range(M-1, -1, -1):  # 열 우선으로 탐색
        for i in range(N-1, -1, -1):
            if arr[i][j] > 0:
                if min_power > arr[i][j]:# 가장 약한 포탑 찾기 뒤에서부터 탐색
                    min_power = arr[i][j]
                    min_loc = [i, j]
                if max_power < arr[i][j]:
                    max_power = arr[i][j]
                    max_loc = [i, j]

    # 공격력 강화!
    x = min_loc[0]
    y = min_loc[1]
    z = max_loc[0]
    k = max_loc[1]

    arr[x][y] = min_power + N + M
    half = arr[x][y] // 2
    # 공격자 찾으러 가기
    path = find_attacker(arr, x, y, z, k)
    # path = [(0, 1), (0, 2), (0, 3), (1, 3), (2, 3)]
    # 레이저 가능하다면 레이저 공격
    if path:
        for i in range(1, len(path)):
            if i == len(path)-1:
                if arr[path[i][0]][path[i][1]] < arr[x][y]:
                    arr[path[i][0]][path[i][1]] = 0
                else:
                    if arr[path[i][0]][path[i][1]] < arr[x][y]:
                        arr[path[i][0]][path[i][1]] = 0
                    else:
                        arr[path[i][0]][path[i][1]] -= arr[x][y]    # 제일 마지막 요소이면 공격력 전부 써서 공격
            else:
                if arr[path[i][0]][path[i][1]] <  half:
                    arr[path[i][0]][path[i][1]] = 0
                else:
                    arr[path[i][0]][path[i][1]] -= half     # 지나가는 요소이면 공격력 절반만 써서 공격
    # 아니라면 포탄 공격
    else:
        if arr[z][k] < arr[x][y]:
            arr[z][k] = 0
        else:
            arr[z][k] -= arr[x][y]  # 중심에 있는 건 공격력 전부 감소
        # 주위 8칸은 절반 힘 감소
        for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)):
            ni = (z + di) % N
            nj = (k + dj) % M
            if arr[ni][nj] > 0 and (ni, nj) != (x, y):
                if arr[ni][nj] < half:
                    arr[ni][nj] = 0
                else:
                    arr[ni][nj] -= half
            else:
                continue

    # 포탑 정비
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                if path is not None and (i, j) not in path:  # path가 None이 아닐 때만 조건 검사
                    arr[i][j] += 1
                elif path is None:  # path가 None이면 그냥 포탑을 정비
                    arr[i][j] += 1

# 가장 큰 포탑의 공격력 구하기
number_1 = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] > number_1:
            number_1 = arr[i][j]

print(number_1)