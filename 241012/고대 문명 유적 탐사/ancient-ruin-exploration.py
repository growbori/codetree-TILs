K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
lst = list(map(int, input().split()))
ans = []
def rotate(arr, si, sj):
    narr = [x[:] for x in arr]
    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j] = arr[si + 3 - 1 -j][sj+i]
    return narr

def bfs(arr, v, si, sj, clr):
    q = []
    q.append((si, sj))
    v[si][sj] = 1
    cnt = 0
    cnt += 1
    fset = set()
    fset.add((si, sj))
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < 5 and 0 <= nj < 5 and v[ni][nj] == 0 and (arr[ni][nj] == arr[ci][cj]):
                cnt += 1
                q.append((ni, nj))
                v[ni][nj] = 1
                fset.add((ni, nj))

    if cnt >= 3:
        if clr == 1:
            for i, j in fset:
                arr[i][j] = 0
        return cnt

    else:
        return 0

def find_you(arr, clr):
    v = [[0] * 5 for _ in range(5)]
    cnt = 0
    for i in range(5):
        for j in range(5):
            if v[i][j] == 0:
                cnt += bfs(arr, v, i, j, clr)
    return cnt

for _ in range(K):
    mx_cnt = 0
    for rot in range(1, 4):
        for sj in range(3):
            for si in range(3):
                narr = [x[:] for x in arr]
                for _ in range(rot):
                    narr = rotate(narr, si, sj)
                t = find_you(narr, 0)
                if mx_cnt < t:
                    mx_cnt = t
                    marr = narr
    if mx_cnt == 0:
        break

    cnt = 0
    arr = marr
    while True:
        t = find_you(arr, 1)
        if t == 0:
            break
        cnt += t

        for j in range(5):
            for i in range(4, -1, -1):
                if arr[i][j] == 0:
                    arr[i][j] = lst.pop(0)

    ans.append(cnt)
print(*ans)