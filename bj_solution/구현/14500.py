n,m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[0*m] for _ in range(n)]
tetro = [[1,1,1,1],
             [[1,1],[1,1]],
             [[1,0],[1,0],[1,1]],
             [[1],[1,1],[0,1]],
             [[1,1,1],[0,1,0]]]