"""
https://leetcode.com/contest/weekly-contest-286/problems/find-the-difference-of-two-arrays/
histogram 그려서 중복여부 탐지. 원소 범위가 [-1000, 1000]밖에 안돼
"""
from typing import List


class Solution:
    COMPLEMENT = 1000

    def __num_to_idx(self, i: int) -> int:
        return i + self.COMPLEMENT

    def __idx_to_num(self, i: int) -> int:
        return i - self.COMPLEMENT

    def __do_solve(self, hist1: list[int], hist2: list[int]) -> list[int]:
        answer = []
        for idx, cnt in enumerate(hist1):
            num = self.__idx_to_num(idx)
            if cnt == 0:
                continue
            # now num is distinct in nums1
            if hist2[self.__num_to_idx(num)] > 0:
                continue
            # now num does not exist in nums2
            answer.append(num)
        return answer

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hist1 = [0] * (self.COMPLEMENT * 2 + 1)
        hist2 = [0] * (self.COMPLEMENT * 2 + 1)
        answer = []

        for e in nums1:
            hist1[self.__num_to_idx(e)] += 1
        for e in nums2:
            hist2[self.__num_to_idx(e)] += 1

        answer.append(self.__do_solve(hist1, hist2))
        answer.append(self.__do_solve(hist2, hist1))

        return answer


class Solution2k
    """
    중복제거를 set을 사용하여 풀 수도 있겠다.
    """
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        answer = []
        answer.append(list(set1 - set2))
        answer.append(list(set2 - set1))

        return answer

