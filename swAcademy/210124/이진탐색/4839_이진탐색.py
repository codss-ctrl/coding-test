import sys

sys.stdin = open("4839_input.txt", "r")


def binary_search(target, left, right):
    cnt = 0
    while True:
        mid = (left + right) // 2
        if target < mid:
            right = mid
        elif target > mid:
            left = mid
        else:
            break
        cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    p, a, b = map(int, input().split())
    midA = binary_search(a, 1, p)
    midB = binary_search(b, 1, p)
    answer = ''
    if midA < midB:
        answer = 'A'
    elif midA > midB:
        answer = 'B'
    else:
        answer = '0'

    print('#{} {}'.format(tc, answer))
