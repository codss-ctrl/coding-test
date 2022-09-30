def solution(queue1, queue2):
    q = queue1 + queue2
    if sum(q) % 2 != 0: return -1
    goal = sum(q)//2
    limit, cnt = len(q) * 2, 0
    left, right = 0, len(queue1)
    s_left = sum(q[left:right])
    while right < len(q) and cnt < limit :
        if s_left < goal:
            s_left += q[right]
            right += 1
        elif s_left > goal:
            s_left -= q[left]
            left += 1
        elif s_left == goal:
            return cnt
        cnt += 1
    return -1

queue1 = [ 1, 1]
queue2 = [ 1, 5 ]
print(solution(queue1,queue2))