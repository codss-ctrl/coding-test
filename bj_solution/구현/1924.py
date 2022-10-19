x,y = map(int, input().split(' '))
cnt = 0
date = ['MON','TUE','WED','THU','FRI','SAT','SUN']
while True:
    if x == 1:
        cnt += y - 1
        break
    if x in [5,7,10,12]:
        cnt += 30
        x -= 1
    elif x in [2,4,6,8,9,11]:
        cnt += 31
        x -= 1
    elif x == 3:
        cnt += 28
        x -= 1
print(date[cnt % 7])