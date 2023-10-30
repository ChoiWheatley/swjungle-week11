"""
https://leetcode.com/contest/weekly-contest-285/problems/count-collisions-on-a-road/

## 풀이법1

"RR" 상황에서 multi_collision을 추가해주자.
"RS" 상황에서 전체 collision의 횟수에 multi_collision을 더하자.

## 풀이법2

1. 충돌걱정이 없는 L, R을 각각 lstrip과 rstrip으로 쳐낸다.
2. stationary 상태의 자동차를 문자열에서 제외한다. (∵ 충돌 카운트가 늘어나지 않기 때문.)
3. 남은 문자들의 개수를 세면 전체 충돌 개수가 튀어나온다. L ⇄ R, R → S, S ← L
"""


class Solution:
    def countCollisions(self, directions: str) -> int:
        d = directions
        return len(d.lstrip("L").rstrip("R").replace("S", ""))

