
N = int(input())
arr = []
for _ in range(N):
    x, y = map(int,input().split(' '))
    arr.append((x,y))
stack = []
for i in range(N):
    cur = arr[i]
    k = 1
    for j in range(N):
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            k += 1
    stack.append(k)
print(*stack)

