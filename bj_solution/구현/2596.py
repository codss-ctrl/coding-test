import sys

rules = ['000000','001111','010011','011100','100110','101001','110101','111010']
n = int(input())
strs = sys.stdin.readline().strip()
res = ''
for i in range(n):
    s = strs[6*i:6*(i+1)]
    if s in rules:
        res += chr(rules.index(s)+65)
    else:
        tmp = ''
        for idx,rule in enumerate(rules):
            diff = bin(int(s,2)^int(rule,2))
            if diff.count('1') == 1:
                tmp += chr(idx+65)
        if tmp:
            res += tmp
        else:
            print(i+1)
            break
else:
    print(res)
