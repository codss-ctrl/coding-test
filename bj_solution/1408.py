import sys
a = sys.stdin.readline()
b = sys.stdin.readline()
s=m=h=0
if b[7:9] < a[7:9]:
    int(b[3:5])-1
    s = 60-a[7:9]
    if b[3:5] < a[3:5]:
        int(b[0:2]) - 1
        m = 60 - a[3:5]
    h = int(b[0:2]) - int(a[0:2])
    print(h,m,s,sep=":")