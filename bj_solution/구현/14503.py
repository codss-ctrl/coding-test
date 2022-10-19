n,m = map(int, input().split())
x,y,d = map(int, input().split())
real_map = [list(map(int,input().split())) for _ in range(n)]
move_map = [[0]*m for _ in range(n)]
move_map[x][y] = 1
dx, dy = [-1,0,1,0], [0,1,0,-1]

def turn_left():
    global d
    d = (d+3)%4

# 처음 위치 청소
cnt = 1
# 회전 횟수
turn_time = 0

while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]
    if move_map[nx][ny] == 0 and real_map[nx][ny] == 0:
        move_map[nx][ny] = 1
        cnt += 1
        x,y = nx,ny
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if real_map[nx][ny] == 0:
            x,y = nx,ny
        else:
            break
        turn_time = 0
print(cnt)
