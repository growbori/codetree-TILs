n = int(input())
cnt = 1
def rec(n):
    global cnt
    for _ in range(n):
        for _ in range(n):
            if cnt < 10:
                print(cnt, end = ' ')
                cnt += 1
            else:
                print(cnt - 9, end = ' ')
                cnt += 1
            
        print()

rec(n)