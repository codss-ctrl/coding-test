t = int(input())
for i in range(t):
    n =int(input())
    arr = list(map(int,input().split()))
    print("#"+str(i+1), max(arr)-min(arr))