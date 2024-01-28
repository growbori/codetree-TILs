n, m = map(int, input().split())
max_list = []
def max_div():
    global max_list
    for i in range(1, m):
        if n % i == 0 and m % i == 0: 
            max_list.append(i)
            i += 1
    
    print(max_list[-1])

max_div()