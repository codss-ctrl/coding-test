import collections

def solution(n, wires):
    if n <= 1 :
        return 0
    result = float('inf')
    graph = collections.defaultdict(list)
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(x, visited):
        visited.add(x)
        for v in graph[x]:
            if v not in visited:
                dfs(v,visited)
        return visited

    for i in graph:
        for j in graph[i]:
            tmp = set()
            tmp.add(i)
            visited = dfs(j, tmp)
            diff = abs(n - (len(visited) - 1) - (len(visited)-1))
            result = min(result, diff)
    return result
n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n,wires))