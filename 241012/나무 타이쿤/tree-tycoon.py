N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
special = []
special.append((N-1, 0))
special.append((N-1, 1))
special.append((N-2, 0))
special.append((N-2, 1))
di = [0, -1, -1, -1, 0, 1, 1, 1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

check = []

def height_plus(check, arr):
    narr = [[0] * N for _ in range(N)]
    dti = [-1, -1, 1, 1]
    dtj = [-1, 1, 1, -1]
    for i in range(len(check)):
        ci, cj = check[i][0], check[i][1]
        for k in range(4):
            ni, nj = ci + dti[k], cj + dtj[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > 0:
                narr[ci][cj] += 1
    for i in range(N):
        for j in range(N):
            arr[i][j] += narr[i][j]
    return arr



for m in range(1, M+1):
    dr, p = map(int, input().split())
    dr = (dr - 1)
    for i in range(len(special)):
        ci, cj = special[i][0], special[i][1]
        ni, nj = (ci + di[dr] * p) % N, (cj + dj[dr] * p) % N
        check.append((ni, nj))
        arr[ni][nj] += 1
    height_plus(check, arr)
    special = []    # special 초기화
    for i in range(N):
        for j in range(N):
            if (i, j) not in check:
                if arr[i][j] >= 2:
                    arr[i][j] -= 2
                    special.append((i, j))
    check = []  # check도 초기화

cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] > 0:
            cnt += arr[i][j]
print(cnt)