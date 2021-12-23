def solution(priorities, location):
    answer = 0
    num = priorities[location]
    max1 = max(priorities)

    for i in priorities:
        if i < max1:
            value = priorities.pop(0)
            priorities.append(value)
        else:
            break

    return priorities

solution([2, 1, 3, 2],2)