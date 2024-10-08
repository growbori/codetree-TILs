L, N, Q = map(int, input().split())
arr = [[2]*(L+2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(L)] + [[2] * (L+2)]
unit = {}
power = [0] * (N+1)
for n in range(1, N+1):
    i, j, h, w, k = map(int, input().split())
    unit[n] = [i, j, h, w, k]
    power[n] = k

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def find_warrior(start, dr):
    q = []
    pset = set()
    q.append(start)
    pset.add(start)
    battle = [0] * (N+1)
    while q:
        cur = q.pop(0)
        ci, cj, h, w, k = unit[cur]
        ni, nj = ci + di[dr], cj + dj[dr]
        for i in range(ni, ni + h):
            for j in range(nj, nj + w):
                if arr[i][j] == 2:
                    return
                if arr[i][j] == 1:
                    battle[cur] += 1
        for idx in unit:
            if idx in pset : continue
            ti, tj, th, tw, tk = unit[idx]
            if ni <= ti + th -1 and ti <= ni+h - 1 and nj <= tj + tw-1 and tj <= nj + w -1:
                q.append(idx)
                pset.add(idx)

    battle[start] = 0
    for idx in pset:
        i, j, h, w, k = unit[idx]
        if k <= battle[idx]:
            unit.pop(idx)
        else:
            ni, nj = i + di[dr], j + dj[dr]
            unit[idx] = [ni, nj, h, w, k-battle[idx]]


for _ in range(Q):
    idx, dr = map(int, input().split())
    if idx in unit:
        find_warrior(idx, dr)

ans = 0
for idx in unit:
    ans += power[idx] - unit[idx][4]

print(ans)