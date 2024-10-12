L, N, Q = map(int, input().split())
arr = [[2] * (L+2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(L)] + [[2] * (L+2)]
units = {}
power = [0] * (N+1)
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for n in range(1, N+1):
    i, j, h, w, k = map(int, input().split())
    units[n] = [i, j, h, w, k]
    power[n] = k


def fight_warrior(start, dr):
    q = []
    q.append(start)
    fset = set()
    fset.add(start)
    damage = [0] * (N+1)
    while q:
        cur = q.pop(0)
        i, j, h, w, k = units[cur]
        ni, nj = i + di[dr], j + dj[dr]
        for si in range(ni, ni + h):
            for sj in range(nj, nj + w):
                if arr[si][sj] == 2:
                    return
                if arr[si][sj] == 1:
                    damage[cur] += 1

        for idx in units:
            if idx in fset: continue
            ti, tj, th, tw, tk = units[idx]
            if ni <= ti + th - 1 and ti <= ni + h - 1 and nj <= tj + tw - 1 and tj <= nj + w - 1:
                q.append(idx)
                fset.add(idx)

    damage[start] = 0
    for idx in fset:
        ci, cj, h, w, k = units[idx]
        if k <= damage[idx]:
            units.pop(idx)
        else:
            ni, nj = ci + di[dr], cj + dj[dr]
            units[idx] = [ni, nj, h, w, k-damage[idx]]


for _ in range(Q):
    idx, dr = map(int, input().split())
    if idx in units:
        fight_warrior(idx, dr)

ans = 0
for idx in units:
    ans += power[idx] - units[idx][4]

print(ans)