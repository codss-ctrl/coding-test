n = int(input())
for i in range(1,n+1):
    cnt = 2*i-1
    space = (2*n-1 - cnt) // 2
    print(' '*space+'*'*cnt)