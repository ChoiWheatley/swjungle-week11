"""
# subarrays distinct element sum of squares

distinct count란? nums[i..j] 범위에서 유일한 원소의 개수

이때, 모든 i,j쌍에 대하여 distinct counts의 제곱을 몽땅 더한 수를 리턴하세요.
"""
from functools import lru_cache
from typing import List


class Solution:
    nums: List[int]

    @lru_cache(10000000)
    def f(self, i: int, j: int) -> int:
        ans = 1
        if i == j:
            print(f"f({i}, {j}) = {ans}")
            return ans  # ∵ 원소가 오직 하나

        add = 1
        if self.nums[j] in self.nums[i:j]:
            add = 0

        c1 = self.f(i, j - 1) + add
        c2 = self.f(i + 1, j)
        ans = max(c1, c2)
        print(f"f({i}, {j}) = {ans}")
        return ans

    def sumCounts(self, nums: List[int]) -> int:
        self.nums = nums

        s = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                s += self.f(i, j) ** 2
        return s


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1]

    print(s.sumCounts(nums))
