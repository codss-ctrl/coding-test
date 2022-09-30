from itertools import permutations
import re

def solution(user_id, banned_id):
    answer = []
    banned_id = [re.sub('\*','.',b) for b in banned_id]
    # ban = ' '.join(banned_id).replace('*','.')
    for p in list(permutations(user_id,len(banned_id))):
        tmp = []
        for i in range(len(banned_id)):
            f = re.match(banned_id[i],p[i])
            if f and len(banned_id[i]) == len(p[i]):
                tmp.append(f.group())
        if len(tmp) == len(banned_id):
            answer.append(sorted(p))
    return set(list(map(tuple,answer))).__len__()
    # return answer
user_id	= ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id =["fr*d*", "abc1**"]

print(solution(user_id,banned_id))