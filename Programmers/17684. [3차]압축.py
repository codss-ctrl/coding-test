def solution(msg):
    answer = []
    dic = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']
    stack = ''
    for m in msg:
        stack+= m
        if stack[-1:] in dic:
            answer.append(dic.index(stack[-1:])+1)
            stack = ''
        else:
            dic.append(''.join(stack[-1:]))
    return dic


msg = 'KAKAO'
print(solution(msg))