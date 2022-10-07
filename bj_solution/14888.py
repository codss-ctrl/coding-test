import sys

input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split())) # +,-.x.%

mini = 1e9
maxi = -1e9

def dfs(idx, total, plus, minus, mul, div):
    global mini,maxi
    if idx == n:
        maxi = max(total,maxi)
        mini = min(total, mini)
        return
    if plus:
        dfs(idx+1, total+num[idx], plus - 1, minus, mul, div)
    if minus:
        dfs(idx+1, total-num[idx], plus, minus-1, mul, div)
    if mul:
        dfs(idx+1, total*num[idx], plus, minus, mul-1, div)
    if div:
        dfs(idx+1, int(total/num[idx]), plus, minus, mul, div-1)

dfs(1, num[0], op[0], op[1], op[2],op[3])
print(maxi)
print(mini)



