n,m = map(int, input().split())
a,b= [],[]
for _ in range(n):
    a.append(list(map(int, input())))
for _ in range(n):
    b.append(list(map(int, input())))

def reverse(i,j):
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            a[x][y] = 1 - a[x][y]

def check():
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
    return True

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            reverse(i,j)
            cnt += 1
if check():
    print(cnt)
else:
    print(-1)
