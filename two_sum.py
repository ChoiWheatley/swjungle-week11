from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        LEN = len(nums)
        m = {}  # (key, value) = (num[i], i)
        for idx, num in enumerate(nums):
            m[num] = idx

        assert len(m) == LEN

        for idx, num in enumerate(nums):
            a = target - num
            if a in m and idx != m[a]:
                return [idx, m[a]]

        return []


if __name__ == "__main__":
    testcases = [
        # (nums, target, expected)
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
    ]
    solution = Solution()
    for nums, target, expected in testcases:
        assert solution.twoSum(nums, target) == expected
