n, k = map(int, input().split(' '))
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)
cnt = 0
for c in coins:
    cnt += k//c
    k %= c
print(cnt)