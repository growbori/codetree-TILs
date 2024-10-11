R, C, K = map(int, input().split())
arr = [[1] + [0] * C + [1] for _ in range(R+3) ]+ [[1] * (C+2)]
units = [list(map(int, input().split())) for _ in range(K)]
exit_set = set()    # 출구 위치만 모아놓은 것

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 높이 구하기 위해 bfs돌림!
def bfs(si, sj):
    q = []
    q.append((si, sj))
    v = [[0] * (C+2) for _ in range(R+4)]
    v[si][sj] = 1
    mx_h = 0
    while q:
        ci, cj = q.pop(0)
        mx_h = max(mx_h, ci)    # ci로 내려갈 수 있는 최대를 구하기!
        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ni, nj = ci + di, cj + dj
            if v[ni][nj] == 0 and ((arr[ni][nj] == arr[ci][cj]) or ((ci, cj) in exit_set and arr[ni][nj] > 1)):
                q.append((ni, nj))
                v[ni][nj] = 1
    return mx_h - 2 # ci가 갈 수 없는 0, R 부분의 값 빼주기!

ans = 0
nums = 2
for cj, dr in units:
    ci = 1
    while True:
        if arr[ci+1][cj-1] == arr[ci+2][cj] == arr[ci + 1][cj+1] == 0:
            ci += 1
        elif arr[ci-1][cj-1] == arr[ci][cj-2] == arr[ci+1][cj-1] == arr[ci + 1][cj-2] == arr[ci + 2][cj-1] == 0:
            ci += 1
            cj -= 1
            dr = (dr-1) % 4 # +- 조심하기!
        elif arr[ci-1][cj+1] == arr[ci][cj+2] == arr[ci+1][cj+1] == arr[ci+1][cj+2] == arr[ci+2][cj+1] == 0:
            ci += 1
            cj += 1
            dr = (dr+1) % 4
        else:
            break

    if ci < 4:
        arr = [[1] + [0] * C + [1] for _ in range(R + 3)] + [[1] * (C + 2)]
        exit_set = set()
    else:
        arr[ci-1][cj] = arr[ci + 1][cj] = nums
        arr[ci][cj-1:cj+2] = [nums] * 3 # 리스트 형태로 받는거 주의하기!
        nums += 1
        exit_set.add((ci + di[dr], cj + dj[dr])) # 출구쪽 좌표 정리해놓기!
        ans += bfs(ci, cj)

print(ans)