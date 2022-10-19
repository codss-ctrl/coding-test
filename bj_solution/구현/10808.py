word = input()
stack = [0 for _ in range(26)]
for w in word:
   stack[ord(w) - ord('a')] += 1
print(*stack)