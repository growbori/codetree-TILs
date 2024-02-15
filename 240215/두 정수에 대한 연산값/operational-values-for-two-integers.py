def calculate(N, M):

    if N > M:
        N = N + 25
        M = M * 2
    else:
        M = M + 25
        N = N * 2

    return N, M

N, M = map(int,input().split())
N, M = calculate(N, M)

print(N, M)