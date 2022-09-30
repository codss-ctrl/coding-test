def base(n,k):
    base = ''
    while n >0:
        n, mod = divmod(n,k)
        base += str(mod)
    return base[::-1]

def prime(n):
    if n == 1 :
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def solution(n, k):
    base_n = base(n,k)
    lst = base_n.split('0')
    answer = 0
    for num in lst:
        if num and prime(int(num)):
            answer += 1
    return answer

n = 437674
k = 3
print(solution(n,k))
