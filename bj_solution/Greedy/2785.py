n = int(input())
chains = list(map(int,input().split()))
chains.sort()
chain_cnt = n
tied = 1
for chain in chains:
    if tied + chain > chain_cnt:
        break
    else:
        chain_cnt -= 1
        tied += chain
print(chain_cnt-1)
