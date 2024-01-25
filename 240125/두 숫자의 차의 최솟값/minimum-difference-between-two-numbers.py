n = int(input())

arr = list(map(int, input().split()))

minminus = 99
for i in range(n-1):
    
    if minminus >= arr[i+1]- arr[i]:
        minminus = arr[i+1]- arr[i]
    
print(minminus)