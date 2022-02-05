import itertools as iter

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [i for i in range(1, 13)]
    combi = [c for c in iter.combinations(arr, n) if sum(c) == k]
    cnt = len(combi)

    print('{}{} {}'.format('#', tc, cnt))
