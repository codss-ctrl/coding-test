
# DFS를 활용한 순열 생성
import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results

# itertools 모듈 사용
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums)) # permutations 모듈은 튜플 반환환
        # return list(map(list, itertools.permutatons(nums)))
        # 리스트로 반환할때는 list로 변경해야함
