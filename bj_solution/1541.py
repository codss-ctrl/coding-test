import sys

strs = sys.stdin.readline().strip().split('-')
result = 0
for s in strs[0].split('+'):
    result += int(s)
for str in strs[1:]:
    for s in str.split('+'):
        result -= int(s)
print(result)