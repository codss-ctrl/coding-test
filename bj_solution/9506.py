while True:
    n = int(input())
    if n == -1:
        break
    else:
        list1 = []
        for i in range(1, n):
            if n % i == 0:
                list1.append(i)

        if sum(list1) == n:
            print(str(n)+' = '+' + '.join(map(str, list1)))
        else:
            print('%d is NOT perfect.' % n)