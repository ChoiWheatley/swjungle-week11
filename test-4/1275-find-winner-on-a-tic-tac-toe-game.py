"""
직접 보드를 그려보고 그 결과를 판독해보자.

판독순서:

- horizontal
- vertical
- decreasing diagonal
- increasing diagonal
"""
from typing import Generator, List

N = 3


def hori(i: int) -> Generator:
    for j in range(N):
        yield (i, j)


def vert(j) -> Generator:
    for i in range(N):
        yield (i, j)


def dec_diag() -> Generator:
    for k in range(N):
        yield (k, k)


def inc_diag() -> Generator:
    for k in range(N):
        yield (N - k - 1, k)


def str_to_result(s: str) -> str:
    if s == "X":
        return "A"
    elif s == "O":
        return "B"
    return ""


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [["" for _ in range(N)] for _ in range(N)]
        turn = True  # 'X' on True, 'O' on False

        for y, x in moves:
            board[y][x] = "X" if turn else "O"
            turn = not turn

        print(board)

        # 승부판별

        for k in range(N):
            # horizontal
            if all(board[i][j] == board[k][0] for i, j in hori(k)):
                bingo = str_to_result(board[k][0])
                if bingo:
                    return bingo

        for k in range(N):
            # vertical
            if all(board[i][j] == board[0][k] for i, j in vert(k)):
                bingo = str_to_result(board[0][k])
                if bingo:
                    return bingo

        # decreasing diag
        if all(board[i][j] == board[0][0] for i, j in dec_diag()):
            bingo = str_to_result(board[0][0])
            if bingo:
                return bingo

        # increasing diag
        if all(board[i][j] == board[2][0] for i, j in inc_diag()):
            bingo = str_to_result(board[2][0])
            if bingo:
                return bingo

        return "Draw" if len(moves) == N * N else "Pending"


if __name__ == "__main__":
    s = Solution()
    testcases = [
        [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]],
        [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]],
        [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]],
        [[0, 0], [1, 1]],
    ]

    for tc in testcases:
        print(s.tictactoe(tc))
