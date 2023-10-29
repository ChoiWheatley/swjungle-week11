from itertools import combinations
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums.sort()

        for i in range(len(nums) - 1):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                # let's do two pointers!
                s = nums[i] + nums[j] + nums[k]

                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    ret.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

        return [list(e) for e in ret]


if __name__ == "__main__":
    testcases = [
        # (nums, expected)
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ]
    s = Solution()

    for t in testcases:
        print(s.threeSum(t[0]))
