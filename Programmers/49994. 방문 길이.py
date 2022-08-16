def solution(dirs):
    x,y = 0,0 # 시작 위치
    table = {
        'U':[0,1],
        'D':[0,-1],
        'L':[-1,0],
        'R':[1,0]
    }  # 테이블에 방향 저장

    def in_range(x, y): # 좌표 경계를 벗어나지 않는지 체크하는 함수
        return -5 <= x <= 5 and -5 <= y <= 5

    visited = set()  # 방문한 루트를 중복되지 않게 저장하기 위해 set 이용
    for dir in dirs:  # 각 명령어마다
        dx, dy = table[dir]  # 명령어에 맞는 x,y 이동방향을 저장
        nx,ny= x+dx, y+dy  # x,y를 이동함
        if in_range(nx,ny):  # 이동한 위치인 nx, ny가 좌표계를 벗어나지 않았다면
            visited.add((x,y,nx,ny))  # 현 위치에서 nx,ny로 가는 루트 저장
            visited.add((nx,ny,x,y))  # nx,ny 에서 현 위치로 가는 루트 저장
            x,y=nx,ny  # x,y를 nx,ny로 저장
    return len(visited) // 2 # 각 길은 두번 저장되어있으므로 2로 나눠줌

dirs = "ULURRDLLU"
print(solution(dirs))