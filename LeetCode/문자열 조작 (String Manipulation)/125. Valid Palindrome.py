# -*- coding: utf-8 -*-
import collections
import re

# 리스트로 변환
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        return True

# 데크 자료형을 이용한 최적화
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

# 슬라이싱 이용
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # 정규식으로 불필요한 문자 필터링
        s = re.sub('[^a-z0-9]','',s)

        return s == s[::-1] # 슬라이싱