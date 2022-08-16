from itertools import combinations as combi


# def solution(relation):
#     row = len(relation)  # 튜플 수
#     col = len(relation[0])  # 칼럼 수
#
#     # 전체 조합
#     candidates = []
#     for i in range(1, col + 1):
#         candidates.extend(combi(range(col), i))
#
#     # 유일성
#     unique = []
#     for candi in candidates:
#         tmp = [tuple([item[i] for i in candi]) for item in relation]
#         if len(set(tmp)) == row:
#             unique.append(candi)
#
#     # 최소성
#     answer = set(unique)
#     for i in range(len(unique)):
#         for j in range(i + 1, len(unique)):
#             if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
#                 answer.discard(unique[j])
#     return len(answer)


from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    # 가능한 속성의 모든 인덱스 조합
    combi = []
    for i in range(1, col + 1):
        combi.extend(combinations(range(col), i))

    # 유일성
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        if len(set(tmp)) == row:  # 유일성
            put = True

            for x in unique:
                if set(x).issubset(set(i)):  # 최소성
                    put = False
                    break

            if put: unique.append(i)

    return len(unique)

relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]

print(solution(relation))