n=int(input())
cnt=1
for i in range(n):
    for j in range(n):
        if 0<cnt<10:
            print(10-cnt,end="")
            cnt+=1
        else:
            print(cnt-1,end="")
            cnt-=8

    print()