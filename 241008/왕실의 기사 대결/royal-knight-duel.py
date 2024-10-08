di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
L, N, Q = map(int, input().split())
arr = [[2] * (L+2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(L)] + [[2] * (L+2)]

units = {}
power = [0] * (N+1)
for m in range(1, N+1):
    i, j, h, w, k = map(int, input().split())
    units[m] = [i, j, h, w, k]
    power[m] = k

def find_damage(start, dr):
    q = []
    q.append(start)
    pset = set()
    pset.add(start)
    damage = [0] *(N+1)
    while q:
        cur = q.pop(0)
        ci, cj, h, w, k = units[cur]
        ni, nj = ci + di[dr], cj + dj[dr]
        for i in range(ni, ni + h):
            for j in range(nj, nj + w):
                if arr[i][j] == 2:
                    return
                if arr[i][j] == 1:
                    damage[cur] += 1
        
        for idx in units:
            if idx in pset:
                continue
            ti, tj, th, tw, tk = units[idx]
            if ni <= ti + th - 1 and ti <= ni + h -1 and nj <= tj + tw -1 and tj <= nj + w -1:
                q.append(idx)
                pset.add(idx)
            
    damage[start] = 0
    for idx in pset:
        si, sj, h, w, k = units[idx]
        if k <= damage[idx]:
            units.pop(idx)
        else:
            ni, nj = si + di[dr], sj + dj[dr]
            units[idx] = [ni, nj, h, w, k-damage[idx]]


for _ in range(Q):
    idx, dr = map(int, input().split())
    if idx in units:
        find_damage(idx, dr)

ans = 0
for idx in units:
    ans += power[idx] - units[idx][4]
print(ans)