class Solution:
    def reverseWords(s) :
        list1 = s.split(" ")
        length = len(list1)
        for i in range(length):
            j = list(list1.pop(0))
            j.reverse()
            i = ''.join(j)
            list1.append(i)
        return " ".join(list1)

# Faster
class Solution:
    def reverseWords(s) :
        return " ".join(x[::-1] for x in s.split())