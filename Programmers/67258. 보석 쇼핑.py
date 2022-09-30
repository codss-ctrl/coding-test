import collections


def solution(gems):
    answer = [0,len(gems)]
    kind = len(set(gems))
    dic = collections.defaultdict(int)
    dic[gems[0]] += 1
    l, r = 0, 0

    while l < len(gems) and r < len(gems):
        if len(dic) < kind:
            r += 1
            if r == len(gems):
                break
            dic[gems[r]] += 1
        else:
            if r-l < answer[1] - answer[0]:
                answer = [l+1, r+1]
            else:
                dic[gems[l]] -= 1
                if dic[gems[l]] == 0:
                    del dic[gems[l]]
                l += 1

    return answer



gems = ["AA", "AB", "AC", "AA", "AC"]
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems = ["XYZ", "XYZ", "XYZ"]
# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))
