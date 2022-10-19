n = int(input())
for i in range(n,0,-1):
    cnt = 2*i-1
    space = (2*n-1-cnt) // 2
    print(' '*space+'*'*cnt)
for i in range(2,n+1):
    cnt = 2*i-1
    space = (2*n-1-cnt) // 2
    print(' '*space+'*'*cnt)