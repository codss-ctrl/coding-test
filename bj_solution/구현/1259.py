while True:
    num = input()
    if int(num) == 0:
        break
    elif num == num[::-1]:
        print('yes')
    else:
        print('no')