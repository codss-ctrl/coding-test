import sys

blank = []
graph = []
for _ in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i,j))

def checkRow(x,num):
    for i in range(9):
        if num == graph[x][i]:
            return False
    return True


def checkCol(y,num):
    for i in range(9):
        if num == graph[i][y]:
            return False
    return True

def checkRect(x,y,num):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if num == graph[nx+i][ny+j]:
                return False
    return True


def dfs(idx):
    if idx == len(blank):
        for i in range(9):
            print(*graph[i])
        exit(0)
    for i in range(1,10):
        x = blank[idx][0]
        y = blank[idx][1]

        if checkRow(x,i) and checkCol(i,y) and checkRect(x,y,i):
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y] = 0
dfs(0)