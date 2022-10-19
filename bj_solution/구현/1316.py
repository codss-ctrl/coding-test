import sys

N = int(input())
cnt = 0
for _ in range(N):
    strs = sys.stdin.readline().strip()
    stack = []
    for s in strs:
        if stack and stack[-1] == s:
            stack.append(s)
        elif stack and s in stack and stack[-1] != s:
            break
        stack.append(s)
    else:
        cnt += 1
print(cnt)