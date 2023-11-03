"""
https://leetcode.com/contest/weekly-contest-320/problems/closest-nodes-queries-in-a-binary-search-tree/

answer[i] = [min_i, max_i]로 이루어진 이차원 배열 answer를 구하는 문제

- min_i: queries[i]보다 작거나 같은 값 중에서 가장 큰 값
- max_i: queries[i]보다 크거나 같은 값 중에서 가장 작은 값

뭐야 BST 탐색이잖아
"""
from typing import List, Optional
from bisect import bisect_left, bisect_right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    """
    tree 직접 순회 +  history 변수

    TLE 💀
    """
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        ret = []

        for e in queries:
            min_i = -1
            max_i = -1

            cur = root
            history = []
            while cur:
                history.append(cur)
                if cur.val < e:
                    cur = cur.right
                elif cur.val > e:
                    cur = cur.left
                else:
                    break
            # print(f"history: {history}")

            for h in reversed(history):
                if h.val <= e:
                    min_i = h.val
                    break

            for h in reversed(history):
                if h.val >= e:
                    max_i = h.val
                    break

            ret.append([min_i, max_i])

        return ret


class Solution2:
    """
    Inorder Travelsal + bisect(다른이의 코드 참고함.)
    """
    sorted_arr: List[int]

    def __init__(self) -> None:
        self.sorted_arr = []

    def __inorder(self, root: Optional[TreeNode]):
        """
        중위순회하여 정렬된 결과를 저장한다.
        """
        if root is None:
            return
        self.__inorder(root.left)
        self.sorted_arr.append(root.val)
        self.__inorder(root.right)



    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        self.__inorder(root)
        nums = self.sorted_arr
        print(f"[*] inorder result: {nums}")
        ret = []

        for q in queries:
            print(f"[*] q = {q}")
            mini = -1
            maxi = -1

            l = 0
            r = len(nums) - 1

            while l <= r:
                # Binary Search
                mid = l + (r - l) // 2
                print(f"[*] nums[{mid}] = {nums[mid]}")
                if nums[mid] > q:
                    maxi = nums[mid]
                    r = mid - 1
                elif nums[mid] < q:
                    mini = nums[mid]
                    l = mid + 1
                else:
                    mini = q
                    maxi = q
                    break

            ret.append([mini, maxi])

        return ret



def arr_to_tree(arr: List[int | None], i: int) -> TreeNode | None:
    if i >= len(arr):
        return None
    if arr[i] is None:
        return None

    root = TreeNode(arr[i])
    left_i = (i << 1) + 1
    right_i = (i << 1) + 2
    
    root.left = arr_to_tree(arr, left_i)
    root.right = arr_to_tree(arr, right_i)

    return root
    


if __name__ == "__main__":
    testcases = [
        {
            "root": [6,2,13,1,4,9,15,None,None,None,None,None,None,14], 
            "queries": [2,5,16]
        },
        {
            "root": [4,None,9],
            "queries": [3]
        },
    ]

    for tc in testcases:
        s = Solution2()
        root = arr_to_tree(tc["root"], 0)
        answer = s.closestNodes(root, tc["queries"])
        print(answer)

    
