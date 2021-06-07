v = int(input())
vote = input()
A=B=0
for i in range(len(vote)):
    if vote[i]=='A':
        A += 1
    else: B+=1
if A > B:
    print("A")
elif A ==B:
    print("Tie")
else: print("B")