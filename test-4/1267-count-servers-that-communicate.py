"""
https://leetcode.com/contest/weekly-contest-164/problems/count-servers-that-communicate/

## idea

connected component?
"""
from itertools import product
from typing import List, Set, Tuple


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])

        res: Set[Tuple[int, int]] = set()

        for i in range(N):
            # horizontal
            s = sum(grid[i])
            # print(f"hori : {[(i, j) for j in range(M) if grid[i][j] > 0]}")
            if s == 1:
                continue
            res = res.union((i, j) for j in range(M) if grid[i][j] > 0)

        for j in range(M):
            # vertical
            s = sum(grid[i][j] for i in range(N))
            # print(f"vert : {[(i, j) for i in range(N) if grid[i][j] > 0]}")
            if s == 1:
                continue
            res = res.union((i, j) for i in range(N) if grid[i][j] > 0)

        return len(res)


class Solution2:
    def countServers(self, grid: List[List[int]]) -> int:
        N = len(grid)
        M = len(grid[0])
        rows = [sum(e) for e in grid]
        cols = [sum(e) for e in zip(*grid)]

        res = 0
        for i, j in product(range(N), range(M)):
            if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
                res += 1

        return res


if __name__ == "__main__":
    s = Solution2()
    testcases = [
        [[1, 0], [0, 1]],
        [[1, 0], [1, 1]],
        [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
        [[1, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0]],
    ]

    for tc in testcases:
        answer = s.countServers(tc)
        print(answer)
