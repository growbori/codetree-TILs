K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(5)]
lst = list(map(int, input().split()))
ans = []
def rotate(arr, si, sj):
    narr = [x[:] for x in arr]
    for i in range(3):
        for j in range(3):
            narr[si+i][sj+j] = arr[si + 3 - 1 - j][sj + i]
    return narr

def bfs(arr, v, si, sj, clr):
    q = []
    q.append((si, sj))
    fset = set()
    fset.add((si, sj))
    v[si][sj] = 1
    cnt = 0
    cnt += 1
    while q:
        ci, cj = q.pop(0)
        for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < 5 and 0 <= nj < 5 and v[ni][nj] == 0 and arr[ci][cj] == arr[ni][nj]:
                q.append((ni, nj))
                cnt += 1
                fset.add((ni, nj))
                v[ni][nj] = 1

    if cnt >= 3:
        if clr == 1:
            for i, j in fset:   # 유물 탐사를 성공한 곳이면 칸을 0으로 바꿔준다!
                arr[i][j] = 0
        return cnt
    else:
        return 0

def find_you(arr, clr):
    v = [[0] * 5 for _ in range(5)] # 먼저 주어주기! 침착하자!
    cnt = 0
    for i in range(5):
        for j in range(5):
            if v[i][j] == 0:
                t = bfs(arr, v, i, j, clr)
                cnt += t
    return cnt

for _ in range(K):
    mx_cnt = 0
    for rot in range(1, 4):
        for sj in range(3):
            for si in range(3):
                narr = [x[:] for x in arr]  # 사용하기 전에 복제하는 것이 좋음!
                for _ in range(rot):
                    narr = rotate(narr, si, sj) # narr로 받는거 주의하기!
                t = find_you(narr, 0)   # narr에서 찾는거 주의! arr에서 찾으면 회전한게 적용 안됨!
                if mx_cnt < t:
                    mx_cnt = t
                    marr = narr
    if mx_cnt == 0:
        break

    cnt = 0
    arr = marr
    while True:
        t = find_you(arr, 1)    # CLR를 flage 처럼 사용!
        if t == 0:
            break
        cnt += t

        for j in range(5):
            for i in range(4, -1, -1):
                if arr[i][j] == 0:
                    arr[i][j] = lst.pop(0)  # pop오류가 나는 원인은 아직 모르겠다,, 
    ans.append(cnt)

print(*ans)