import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0]*n
dp[0] = arr[0]
for i in range(1,n): # 앞 수와 연속되는 경우, 현재 수만 선택
    dp[i] = max(dp[i-1]+arr[i],arr[i])
print(max(dp))