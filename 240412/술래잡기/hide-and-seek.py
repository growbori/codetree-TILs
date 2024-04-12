def catcher(arr):
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    mx_cnt, cnt, flag, val = 1, 0, 0, 1
    M = n//2
    si, sj, td = M, M, 0
    k = 1
    cnt += 1
    arr[si][sj] = 2
    ti, tj = si + di[td], sj + dj[td]
    if (ti, tj) == (1, 1):
        mx_cnt, cnt, flag, val = N, 1, 1, -1
        td = 2
    elif (ti, tj) == (M, M):
        mx_cnt, cnt, flag, val = 1, 0, 0, -1
        td = 0
    else:
        if cnt == mx_cnt:
            arr[si][sj] , arr[ti][tj] = arr[ti][tj], arr[si][sj]
            cnt = 0
            td = (td+val) % 4
            if flag == 0:
                flag = 1
            else:
                flag = 0
                mx_cnt += val
    return td

#도망자의 이동 나타내는 함수
def runner(arr):
    global  q
    ver_di = [0, 0]
    ver_dj = [-1, 1]
    hor_di = [-1, 1]
    hor_dj = [0, 0]
    # visited = [[0] * n for _ in range(n)]   # 한번 방문했던 지점을 또 방문해도 무방하다! 고로 사용 안함!
    # visited[ci][cj] = 1
    while q:
        ci, cj = q.pop(0)
        for u in range(2):
            if abs(si - ci) + abs(sj - cj) <= 3:  # 술래와 도망자 사이의 거리가 3 이하일때만 이동
                if arr[ci][cj] != 0 and arr[ci][cj] == (1, 1):
                    u = (u+1) % 2   # 방향 전환
                    ni = ci + ver_di[u]
                    nj = cj + ver_dj[u]
                    # 방향 전환 어떻게 하지??
                    # 단, 이동 도중 도망자들의 위치는 겹칠 수 있음에 유의합니다. 이걸 구현을 못해서 sort해서 뒤에서부터 작업했음
                    if 0 <= ni < n and 0 <= nj < n:
                        arr[ci][cj] = 0
                        arr[ni][nj] = ((1, 1))
                    else:
                        u += 1
                        ni = ci + ver_di[u]
                        nj = cj + ver_dj[u]
                        arr[ci][cj] = 0
                        arr[ni][nj] = ((1, 1))
                elif arr[ci][cj] != 0 and arr[ci][cj] == (1, 2):
                    u = (u + 1) % 2  # 방향 전환
                    ni = ci + hor_di[u]
                    nj = cj + hor_dj[u]
                    if 0 <= ni < n and 0 <= nj < n:
                        arr[ci][cj] = 0
                        arr[ni][nj] = ((1, 2))
                    else:
                        u += 1
                        ni = ci + ver_di[u]
                        nj = cj + ver_dj[u]
                        arr[ci][cj] = 0
                        arr[ni][nj] = ((1, 2))
    return


n, m, h, k = map(int, input().split())
arr = [[0] * (n) for _ in range(n)]

# 술래의 초기 위치 배치하기
for i in range(n):
    for j in range(n):
        si, sj = n//2, n//2
        arr[si][sj] = 2     # 술래 배치

# 도망자의 초기 위치 배치하기
for _ in range(m):
    x, y, d = map(int, input().split())
    for _ in range(n):
        for _ in range(n):
            arr[x-1][y-1] = (1, d)


#나무의 초기 위치 배치하기
tree_loc = [[0] * n for _ in range(n)]
for _ in range(h):
    tree_x, tree_y = map(int, input().split())
    for _ in range(n):
        for _ in range(n):
            tree_loc[tree_x-1][tree_y-1] = 1
# print(tree_loc)
# 도망자의 위치 전부 가져오기 ( 뒤에서 부터 생각! )
q = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0 and arr[i][j] != 2:
            q.append((i, j))
            q.sort(reverse=True)
# print(arr)
count = 0
# k 초 동안 반복할 예정
for _ in range(k):
    runner(arr)
    dr = catcher(arr)
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    for i in range(n):
        for j in range(n):
            for k in range(1, 3):
                if arr[i][j] == 2:  # 술래가 있는 자리
                    ni, nj = i + di[dr] * k, j + dj[dr] * k
                    if 0 <= ni < n and 0 <= ni < n and arr[ni][nj] != 0 and tree_loc[ni][nj] == 0:  # 나무 없이 술래의 시야에 있으면
                        count += 1
                        arr[ni][nj] = 0
    print(count)