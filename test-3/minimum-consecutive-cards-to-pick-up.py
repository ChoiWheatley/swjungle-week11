"""
https://leetcode.com/contest/weekly-contest-291/problems/minimum-consecutive-cards-to-pick-up/
"""
from math import inf
from typing import List


class Solution:
    """TLE(O(N ** 2))"""

    NOTFOUND = 1 << 31 - 1

    def minimumCardPickup(self, cards: List[int]) -> int:
        ret = self.NOTFOUND
        i = 0

        for i in range(len(cards) - 2):
            j = i + 1
            while i < j and j < len(cards):
                # print(f"i: {i}, j: {j}")
                if cards[i] == cards[j]:
                    ret = min(ret, j - i + 1)
                    break
                else:
                    j += 1

        return ret if ret != self.NOTFOUND else -1


if __name__ == "__main__":
    INPUT = [
        95,
        11,
        8,
        65,
        5,
        86,
        30,
        27,
        30,
        73,
        15,
        91,
        30,
        7,
        37,
        26,
        55,
        76,
        60,
        43,
        36,
        85,
        47,
        96,
        6,
    ]
    s = Solution()
    print(s.minimumCardPickup(INPUT))


class Solution2:
    """
    ```python
    if len(set(cards)) == len(cards):
        return -1
    ```

    for문 돌면서 dic에 `nums[i]`에 그 인덱스 `i`를 넣어준다. (계속 갱신)
    카드의 숫자가 dic에 존재하면 `ans = min(ans, i - dic[nums[i]] + 1)`
    """

    NOTFOUND = 1 << 31 - 1

    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(set(cards)) == len(cards):
            # no duplicates
            return -1
        dic = {}
        ans = self.NOTFOUND
        for i, e in enumerate(cards):
            if e in dic:
                ans = min(ans, i - dic[e] + 1)
            dic[e] = i
        return ans

