import sys

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
strs = sys.stdin.readline().strip()
cnt = 0
for s in strs:
    for i in range(len(dial)):
        if s in dial[i]:
            cnt += i+3
print(cnt)
