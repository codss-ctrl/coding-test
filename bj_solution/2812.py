n,k = map(int, input().split(' '))
num = list(input())
K, stack = k, []
for i in range(n):
    while stack and K > 0 and stack[-1] < num[i]:
        stack.pop()
        K -= 1
    stack.append(num[i])

print(''.join(stack[:n-k]))