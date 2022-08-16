import collections, math


def solution(n, words):
    answer = [0, 0]
    stack = []
    for i, word in enumerate(words):
        if not stack:
            stack.append(word)
            continue

        if stack:
            if stack[-1][-1] == word[0] and word not in stack:
                stack.append(word)

            elif stack[-1][-1] != word[0] or word in stack:
                number = (i+1) % n
                if number % n == 0:
                    number = n
                rnd = math.ceil((i+1) / n)
                answer = [number, rnd]
                break


    return answer

n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]
print(solution(n, words))
