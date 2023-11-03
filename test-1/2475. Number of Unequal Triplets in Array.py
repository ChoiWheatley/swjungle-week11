"""
https://leetcode.com/contest/weekly-contest-320/problems/number-of-unequal-triplets-in-array/
i < j < k && [i] != [j] != [k] 를 만족하는 triplet (i, j, k)의 개수를 구하는 문제

## example 1:

        0 1 2 3 4
nums = [4,4,2,4,3]
expected = [
    (0, 2, 4),
    (1, 2, 4),
    (2, 3, 4)
]
"""
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        N = len(nums)
        ret = 0

        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[k] != nums[i]:
                        ret += 1
            

        return ret


