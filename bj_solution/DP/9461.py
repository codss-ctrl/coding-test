t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 3:
        print(1)
        continue
    if n == 4:
        print(2)
        continue
    dp = [0]*(n+1)
    dp[0]=0
    dp[1]=1
    dp[2]=1
    dp[3]=1
    dp[4]=2
    for i in range(5,n+1):
        dp[i] = dp[i-1]+dp[i-5]
    print(dp[n])