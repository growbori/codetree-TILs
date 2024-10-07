'''
주위 2로 둘러싸기
밀린 처리 : 명령 받은 기사가 다음 위치 (범위) - 모든 기사 겹침 체크
범위가 겹치면 -> q 추가 q에서 하나씩 쪼개서 처리
이동대상 pset <= set() 추가
units = {1 : [1, 2, 2, 1, 2], 2 : []}
pset의 units를 dr 방향으로 한칸 이동
unit 삭제 처리
'''

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
N, M, Q = map(int, input().split())
#벽으로 둘러싸기
arr = [[2] * (N+2)] + [[2] + list(map(int, input().split())) + [2] for _ in range(N)] + [[2] * (N+2)]
units = {}  # 딕셔너리 형태로 저장
init_k = [0] * (M+1)    # 초기 체력 저장 용
for m in range(1, M+1):
    si, sj, h, w, k = map(int, input().split())
    units[m] = [si, sj, h, w, k]
    init_k[m] = k   # 초기 체력 저장

def push_unit(start, dr):   # s를 밀고, 연쇄처리
    q = []  # 밀 후보를 저장
    pset = set()    # 이동 기사 번호 저장
    damage = [0] * (M+1)    # 각 유닛 별 데미지 누적
    q.append(start) # 초기 데이터 저장
    pset.add(start)

    while q:
        cur = q.pop(0)  # q에서 데이터 한개 꺼냄
        ci, cj, h, w, k = units[cur]

        # 명령 받은 방향 진행, 벽이 아니고, 겹치는 다른 조각이면 q에 저장
        ni, nj = ci + di[dr], cj + dj[dr]
        for i in range(ni, ni + h):
            for j in range(nj, nj + w):
                if arr[i][j] == 2:  # 벽을 만날 경우 밀 수 없으므로 return
                    return  # 무조건 리턴! break 아님!
                if arr[i][j] == 1:  # 함정인 경우
                    damage[cur] += 1    # 데미지 누적

        # 겹치는 다른 유닛이 있는 경우 큐에 추가 ( 모든 유닛 체크)
        for idx  in units:
            if idx in pset: continue # 이미 움직일 대상이면 체크할 필요 없음

            ti, tj, th, tw, tk = units[idx]

            # 겹치는 경우
            if ni <= ti + th - 1 and ni + h - 1 >= ti and tj <= nj + w - 1 and nj <= tj + tw - 1:
                q.append(idx)
                pset.add(idx)

    # 명령 받은 기사는 데미지 입지 않음
    damage[start] = 0
    #  이동, 데미지가 체력 이상이면 삭제 처리
    for idx in pset:
        si, sj, h, w, k = units[idx]
        if k <= damage[idx] : # 체력보다 받은 데미지가 크다면 삭제
            units.pop(idx)
        else:
            ni, nj = si + di[dr], sj + dj[dr]
            units[idx] = [ni, nj, h, w, k-damage[idx]]


for _ in range(Q):
    idx, dr = map(int, input().split())
    if idx in units:
        push_unit(idx, dr)  # 명령 받은 기사 (연쇄적으로 밀기 : 벽이 없는 경우까지)

ans = 0
for idx in units:
    ans += init_k[idx] - units[idx][4]

print(ans)