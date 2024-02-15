def calculate(N, M):

    if N > M:
        N = N + 25
        M = M * 2
    else:
        M = M + 25
        N = N * 2

    print(N, M)

N, M = map(int,input().split())
calculate(N, M)