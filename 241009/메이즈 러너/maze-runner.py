# 이동

# 회전

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for _ in range(M):
    i, j = map(lambda x : int(x)-1, input().split())
    arr[i][j] -= 1  # 사람 배치
ei, ej = map(lambda x : int(x)-1, input().split())
arr[ei][ej] = -11   # 출구 배치

ans = 0 # 이동거리 합
cnt = M # 참가자 수

def make_square(arr):
    mn = N
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0:
                mn = min(mn, max(abs(ei - i), abs(ej -j)))
    for si in range(N-mn) :     # 시작점 찾기
        for sj in range(N-mn):
            if si <= ei <= si + mn and sj <= ej <= sj + mn:
                for i in range(si, si + mn + 1):
                    for j in range(sj, sj + mn + 1):
                        if - 11 < arr[i][j] < 0:
                            return si, sj, mn + 1

def find_exit():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == -11:
                return i, j

for _ in range(K):
    narr = [x[:] for x in arr]
    for i in range(N):
        for j in range(N):
            if -11 < arr[i][j] < 0:
                dist = abs(ei - i) + abs(ej - j)
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] <= 0 and dist > abs(ei - ni) + abs(ej - nj):
                        ans += arr[i][j]
                        narr[i][j] -= arr[i][j]
                        if arr[ni][nj] == -11:
                            cnt += arr[i][j]
                        else:
                            narr[ni][nj] += arr[i][j]
                        break
    arr = narr

    if cnt == 0:    # 모든 참가자가 미로를 탈출한 경우
        break

    si, sj, L = make_square(arr)

    # 회전하기
    narr = [x[:] for x in arr]
    for i in range(L):
        for j in range(L):
            narr[si + i][sj + j] = arr[si + L -1 - j][sj + i]
            if narr[si + i][sj + j] > 0:
                narr[si + i][sj + j] -= 1   # 내구도 깎임

    arr = narr

    ei, ej = find_exit()

print(-ans)
print(ei + 1, ej + 1)