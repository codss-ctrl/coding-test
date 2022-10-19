num = input()
card = [0 for _ in range(10)]
for n in num:
    if int(n) in [6,9]:
        if card[6] <= card[9]:
            card[6] += 1
        else:
            card[9] += 1
    else:
        card[int(n)] += 1

print(max(card))