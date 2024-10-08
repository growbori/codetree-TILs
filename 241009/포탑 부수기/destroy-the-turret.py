N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
turn = [[0] * M for _ in range(N)]
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


for T in range(1, K + 1):
    cnt = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                cnt += 1
    if cnt == 1:    # 0 이 아닌 포탑의 갯수 세기 -> 1이면 종료
        break
    mn, mx_turn, x, y = 5001, 0, -1, -1
    for i in range(N):
        for j in range(M):
            if arr[i][j] <= 0:    continue  # 포탑이 아니면 skip
            if mn > arr[i][j] or (mn == arr[i][j] and mx_turn < turn[i][j]) or \
                    (mn == arr[i][j] and mx_turn == turn[i][j] and x + y < i + j) or \
                    (mn == arr[i][j] and mx_turn == turn[i][j] and x + y == i + j and y < j):
                mn, mx_turn, x, y = arr[i][j], turn[i][j], i, j  # si,sj 공격자

    # [2] 공격(공격당할 포탑선정) & 포탑부서짐
    # 2-1) 공격 당할 포탑 선정: 공격력 높은->가장 오래전 공격->행+열(작은)->열(작은)
    mx, mn_turn, z, k = 0, T, N, M
    for i in range(N):
        for j in range(M):
            if arr[i][j] <= 0:    continue  # 포탑이 아니면 skip
            if mx < arr[i][j] or (mx == arr[i][j] and mn_turn > turn[i][j]) or \
                    (mx == arr[i][j] and mn_turn == turn[i][j] and z + k > i + j) or \
                    (mx == arr[i][j] and mn_turn == turn[i][j] and z + k == i + j and k > j):
                mx, mn_turn, z, k = arr[i][j], turn[i][j], i, j  # ei,ej 공격대상자

    # 공격력 강화!


    arr[x][y] = mn + N + M
    turn[x][y]=T
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