n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
dp = [0]*10000
dp[0] = arr[0]
dp[1] = arr[0]+arr[1]
dp[2] = max(arr[0]+arr[2], arr[2]+arr[1],dp[1])
for i in range(3,n): # 현재 와인을 마시지 않는 경우도 생각
    dp[i] = max(arr[i-2]+arr[i], arr[i]+arr[i-1]+dp[i-3],dp[i-1])
print(max(dp))