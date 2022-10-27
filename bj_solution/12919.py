import sys

def make(c):
    global flag
    if len(c) == len(s):
        if c == s:
            flag = True
        return

    if c[0] =='B':
        c=c[::-1]
        c.pop()
        make(c)
        c.append("B")
        c=c[::-1]
    if c[-1] == 'A':
        c.pop()
        make(c)
        c.append('A')

input = sys.stdin.readline
s = list(str(input().strip()))
t = list(map(str, input().strip()))
flag = False
make(t)

print(1) if flag else print(0)