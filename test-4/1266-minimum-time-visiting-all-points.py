"""
https://leetcode.com/contest/weekly-contest-164/problems/minimum-time-visiting-all-points/
"""

from typing import List


def seconds_to_move(p1: List[int], p2: List[int]) -> int:
    delta_y = abs(p2[0] - p1[0])
    delta_x = abs(p2[1] - p1[1])
    manhattan = delta_y + delta_x
    diag = min(delta_y, delta_x)

    return manhattan - diag


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        s = 0
        for i in range(len(points) - 1):
            s += seconds_to_move(points[i], points[i + 1])
        return s
