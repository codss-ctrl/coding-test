from collections import deque

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    q = deque(arr)
    stack = []
    while len(q) > 0:
        stack.append(q.pop())  # 가장 큰 수
        stack.append(q.popleft())  # 가장 작은 수
        if len(stack) == 10:
            break
    print('{}{} {}'.format('#', tc, ' '.join(map(str, stack))))
