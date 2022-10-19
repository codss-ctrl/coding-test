dic = {1:'A',2:'B',3:'C',4:'D',0:'E'}

for _ in range(3):
    l = input().split(' ')
    print(dic[l.count('0')])
