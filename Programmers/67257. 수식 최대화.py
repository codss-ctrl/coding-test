from itertools import permutations

def solution(expression):
    answer = []
    sign = ['*','+','-']
    for p in permutations(sign):
        fst, snd = p[0],p[1]
        lst = []
        for e in expression.split(fst):
            tmp = [f'({i})' for i in e.split(snd)]
            lst.append(f'({snd.join(tmp)})')
        answer.append(abs(eval(fst.join(lst))))
    return max(answer)