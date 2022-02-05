T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    mx = float('-inf')  # 음수
    mn = float('inf')  # 양수
    for j in range(n - m + 1):
        mx = max(mx, sum(arr[j: j + m]))
        mn = min(mn, sum(arr[j: j + m]))
        result = mx - mn
    print('#' + str(i), result)


