"""
https://leetcode.com/contest/weekly-contest-164/problems/search-suggestions-system/
"""
from typing import List
import re


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """
        regex solution
        Runtime: 2311 ms 💀
        Memory Usage: 23.7 MB
        """
        ret = []
        products.sort()

        for end in range(1, len(searchWord) + 1):
            substr = searchWord[:end]
            pattern = re.compile(f"^{substr}")
            search_result = [x for x in products if pattern.search(x) is not None][:3]

            print(search_result)
            ret.append(search_result)

        return ret


if __name__ == "__main__":
    s = Solution()
    testcases = [
        {"products": ["mobile", "mouse", "moneypot", "monitor", "mousepad"], "searchWord": "mouse"}
    ]

    for tc in testcases:
        answer = s.suggestedProducts(**tc)
        print(f"answer: {answer}")
