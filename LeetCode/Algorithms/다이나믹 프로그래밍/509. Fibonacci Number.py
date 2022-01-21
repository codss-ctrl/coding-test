# 재귀 구조 브루트 포스
import collections


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


# 메모이제이션
class Solution:
    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.dp[n]


# 타뷸레이션
class Solution:
    dp = collections.defaultdict(int)

    def fib(self, n: int) -> int:
        self.dp[0] = 0
        self.dp[1] = 1

        for i in range(2, n + 1):
            self.dp[i] = self.fib[i - 1] + self.fib(i - 2)
        return self.dp[n]


# 두 변수만 이용해 공간 절약
class Solution:
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for i in range(2, n + 1):
            x, y = y, x + y
        return x


# 행렬 -> numpy 사용으로 리트코드에서는 동작하지 않음
import numpy as np


class Solution:
    def fib(self, n: int) -> int:
        M = np.matrix([[0, 1], [1, 1]])
        vec = np.array([[0], [1]])

        return np.matmul(M ** n, vec)[0]
