import re

# 효율성 x
# def bfs(candidate, conditions):
#
#     for i in range(len(conditions)):
#         condition = conditions[i]
#         info = candidate[i]
#
#         if condition == '-':
#             continue
#         if info.isalpha() and condition.isalpha() and info != condition:
#             return False
#         if info.isdigit() and condition.isdigit() and int(condition) > int(info):
#             return False
#
#     return True
#
# def solution(info, query):
#     answer = []
#     infos = []
#     for i in info:
#         infos.append(i.split(' '))
#
#     for q in query:
#         cnt = 0
#         conditions = re.split(r" and |\s", q)
#         for candidate in infos:
#             if not bfs(candidate, conditions):
#                 continue
#             else:
#                 cnt += 1
#         answer.append(cnt)
#
#     return answer

# 출처 https://programmers.co.kr/questions/27124
import bisect, itertools, collections

def solution(info, query):
    infomap = collections.defaultdict(list)
    binarys = list(itertools.product((True, False), repeat=4))
    for inf in info:
        inf = inf.split()
        for binary in binarys:
            key = ''.join([inf[i] if binary[i] else '-' for i in range(4)])
            infomap[key].append(int(inf[4]))

    for k in infomap.keys():
        infomap[k].sort()

    answers = []
    for q in query:
        l,_,p,_,c,_,f, point = q.split()
        key = ''.join([l,p,c,f])
        i = bisect.bisect_left(infomap[key], int(point))
        answers.append(len(infomap[key]) - i)

    return answers
info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]

print(solution(info,query))