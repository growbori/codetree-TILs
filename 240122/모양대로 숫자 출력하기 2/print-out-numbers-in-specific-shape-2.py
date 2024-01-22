n=int(input())
cnt=8
for i in range(n):
    for j in range(n):
        if 1<cnt<10:
            print(10-cnt,end=" ")
            cnt-=2
        else:
            print(cnt+2,end=" ")
            cnt+=6

    print()