n = int(input())
level = []
for _ in range(n):
    level.append(int(input()))
level[:] = level[::-1]
cnt = 0
stack = []
for i in range(n):
    while stack and stack[-1] <= level[i]:
        level[i] -= 1
        cnt += 1
    stack.append(level[i])

print(cnt)