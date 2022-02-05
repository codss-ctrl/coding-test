import sys

sys.stdin = open("색칠하기_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    # cnt =0
    # canvas = [[0] * 10 for _ in range(10)] # 10x10 캔버스
    # N = int(input())
    # colors = [[0] * 5 for _ in range(N)] # [x][y][x][y][색]
    # for n in range(N):
    #     colors[n] = list(map(int, input().split()))
    #
    # for color in colors:
    #     for row in range(color[0], color[2]+1):
    #         for column in range(color[1], color[3]+1):
    #             if canvas[row][column] == 0:
    #                 canvas[row][column] = color[4]
    #             elif canvas[row][column] != 3 and canvas[row][column] != color[4]:
    #                 canvas[row][column] = 3
    #                 cnt += 1
    # print('{}{} {}'.format('#',tc,cnt))

    N = int(input())
    location = [set({}),set({})] # 색상 1,2 위치 저장, 내부값은 셋
    # 케이스만큼 반복
    for n in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        # x,y 를 돌면서 set에 넣음
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                location[color-1].add((x,y))
        # 교집합을 이용해 겹치는 부분만 꺼냄
        result = location[0] & location[1]
        # 겹치는 만큼 출력
        print('#{} {}'.format(tc, len(result)))


