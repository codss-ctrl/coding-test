import collections

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for i in range(1, T + 1):
    n = int(input())
    arr = list(map(int,input()))
    counts = collections.Counter(arr)

    if counts.most_common(1)[0][1] == 1:  # [[5, 2]]
        result = max(arr)
    else:
        result = counts.most_common(1)[0][0]
    print('#' + str(i), result, counts.most_common(1)[0][1])
