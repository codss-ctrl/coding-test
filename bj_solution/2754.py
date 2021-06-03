c = input()
pre = c[0]
post = c[1:]
if pre == 'A':
    if post == '+':
        print(4.3)
    elif post == '0':
        print(4.0)
    else: print(3.7)
if pre == 'B':
    if post == '+':
        print(3.3)
    elif post == '0':
        print(3.0)
    else: print(2.7)
if pre == 'C':
    if post == '+':
        print(2.3)
    elif post == '0':
        print(2.0)
    else: print(1.7)
if pre == 'D':
    if post == '+':
        print(1.3)
    elif post == '0':
        print(1.0)
    else: print(0.7)
if pre == 'F':
    print(0.0)

c = input()
grade = {
    'A+': 4.3,
    'A0': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B0': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C0': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D0': 1.0,
    'D-': 0.7,
    'F': 0.0,
}
print(grade[c])