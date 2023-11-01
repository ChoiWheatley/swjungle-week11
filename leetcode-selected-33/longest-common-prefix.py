"""
https://leetcode.com/problems/longest-common-prefix/
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if any(len(s) == 0 for s in strs):
            return ""

        minlen = min(len(s) for s in strs)
        l = 0
        while l < minlen and all(s[l] == strs[0][l] for s in strs):
            l += 1
        return strs[0][:l]


if __name__ == "__main__":
    s = Solution()
    testcases = [(["a"], "a"), ([""], "")]

    for strs, expected in testcases:
        answer = s.longestCommonPrefix(strs)
        print(f"({strs}, {expected}) ⟶ {answer} {'✅' if answer == expected else '❌'}")
