def solution(skill, skill_trees):
    dic = {}
    for i in range(len(skill)-1):
        dic[skill[i]].append(skill[i+1])
    answer = -1
    return answer