n = int(input())
graph = [[0,[]] for _ in range(n+1)]
graph[1][0] = 0
graph[1][1] = [1]
for i in range(2,n+1):
    #-1
    graph[i][0] = graph[i-1][0]+1
    graph[i][1] = graph[i-1][1]+[i]
    # //3
    if i % 3 == 0 and graph[i//3][0] + 1< graph[i][0]:
        graph[i][0]= graph[i//3][0]+1
        graph[i][1] = graph[i//3][1]+[i]
    if i % 2 == 0 and graph[i // 2][0] + 1 < graph[i][0]:
        graph[i][0] = graph[i // 2][0] + 1
        graph[i][1] = graph[i // 2][1] + [i]
print(graph[n][0])
print(*graph[n][1][::-1])