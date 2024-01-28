n = int(input())
cnt = 1
def rec(n):
    global cnt
    for _ in range(n):
        for _ in range(n):
            if 1<cnt<10:
                print(10-cnt+1,end=" ")
                cnt-=1
            else:
                print(1,end=" ")
                cnt+=8

        print()

rec(n)