N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
turn = [[0] * M for _ in range(N)]  # 공격한 턴수를 기록(최근공격 체크)

def count_potap():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                cnt += 1
    return cnt

def bfs(si, sj, ei, ej):
    q = []
    q.append((si, sj))
    v = [[[] for _ in range(M)] for _ in range(N)]
    v[si][sj] = (si, sj)
    while q:
        ci, cj = q.pop(0)
        if (ci, cj) == (ei, ej):
            arr[ei][ej] = max(0, arr[ei][ej] - damage)
            while True:
                ci, cj = v[ci][cj]
                if (ci, cj) == (si, sj):
                    return True
                arr[ci][cj] = max(0, arr[ci][cj] - half)
                fset.add((ci, cj))
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = (ci + di) % N, (cj + dj) % M
            if arr[ni][nj] > 0 and len(v[ni][nj]) == 0:
                q.append((ni, nj))
                v[ni][nj] = (ci, cj)
    return False

def bomb(si, sj, ei, ej):
    arr[ei][ej] = max(0, arr[ei][ej] - damage)
    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)):
        ni, nj = (ei + di) % N, (ej + dj) % M
        if (si, sj) != (ni, nj) and arr[ni][nj] > 0:
            arr[ni][nj] = max(0, arr[ni][nj] - half)
            fset.add((ni, nj))

for T in range(1, K + 1):
    t = count_potap()
    if t == 1:
        break
    else:
    # [1] 공격자 선정: 공격력 낮은->가장 최근 공격자->행+열(큰)->열(큰)
        mn, mx_turn, si, sj = 5001, 0, -1, -1
        for i in range(N):
            for j in range(M):
                if arr[i][j]<=0:    continue    # 포탑이 아니면 skip
                if mn>arr[i][j] or (mn==arr[i][j] and mx_turn<turn[i][j]) or \
                    (mn==arr[i][j] and mx_turn==turn[i][j] and si+sj<i+j) or \
                    (mn==arr[i][j] and mx_turn==turn[i][j] and si+sj==i+j and sj<j):
                    mn, mx_turn, si, sj = arr[i][j], turn[i][j], i, j   # si,sj 공격자

        # [2] 공격(공격당할 포탑선정) & 포탑부서짐
        # 2-1) 공격 당할 포탑 선정: 공격력 높은->가장 오래전 공격->행+열(작은)->열(작은)
        mx, mn_turn, ei, ej = 0, T, N, M
        for i in range(N):
            for j in range(M):
                if arr[i][j]<=0:    continue    # 포탑이 아니면 skip
                if mx<arr[i][j] or (mx==arr[i][j] and mn_turn>turn[i][j]) or \
                    (mx==arr[i][j] and mn_turn==turn[i][j] and ei+ej>i+j) or \
                    (mx==arr[i][j] and mn_turn==turn[i][j] and ei+ej==i+j and ej>j):
                    mx, mn_turn, ei, ej = arr[i][j], turn[i][j], i, j   # ei,ej 공격대상자

        arr[si][sj] += (N+M)
        damage = arr[si][sj]
        half = damage // 2
        turn[si][sj] = T
        fset = set()
        fset.add((si, sj))
        fset.add((ei, ej))

        if bfs(si, sj, ei, ej) == False:
            bomb(si, sj, ei, ej)

        for i in range(N):
            for j in range(M):
                if arr[i][j] > 0 and (i, j) not in fset:
                    arr[i][j] += 1

number_1 = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] > number_1:
            number_1 = arr[i][j]
print(number_1)