n, m = map(int, input().split())

minmul_list = []

def minmul():
    global minmul_list
    for i in range(1, 10001):
        if i % n == 0 and i % m == 0:
            minmul_list.append(i)
            i += 1
    print(minmul_list[0])

minmul()