"""
https://leetcode.com/contest/weekly-contest-291/problems/remove-digit-from-number-to-maximize-result/
일단 하나씩 빼보면서 max를 구해보자
"""
DEBUG = True


def dbg(s: str):
    if DEBUG:
        print(s)


class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ret = ""
        for idx, c in enumerate(number):
            if c == digit:
                tmp = number[:idx] + number[idx + 1 :]
                ret = max(ret, tmp)

        return ret


def str_remove_at(s: str, idx: int) -> str:
    return s[:idx] + s[idx + 1 :]


class Solution2:
    """
    digit보다 큰 숫자가 digit 뒤에 나타나는 경우가 최대.
    [1,3,3,1,7,3,2], digit = 3 을 예시로 들면, 처음 두 3을 제거하게 되면
    131732가 되고, 세번째 3을 제거하게 되면 133172가 되므로 전자가 더 크게 된다.
    24ms 16.17MB
    """

    def removeDigit(self, number: str, digit: str) -> str:
        found = -1
        maxstr = ""
        for i in range(len(number)):
            n = number[i]

            if digit == n:
                found = i
            if digit < n and found != -1:
                maxstr = max(maxstr, str_remove_at(number, found))

        return max(maxstr, str_remove_at(number, found))


class Solution3:
    """
    digit 바로 뒤에 있는 원소만 보면 되는 것이었다... 🙊
    37ms 16.23MB
    """

    def removeDigit(self, number: str, digit: str) -> str:
        found = -1
        for i in range(len(number) - 1):
            if number[i] == digit:
                found = i
            if number[i] == digit and digit < number[i + 1]:
                # 바로 오른쪽 원소하고만 대소비교한다.
                return str_remove_at(number, i)

        if number[-1] == digit:
            found = len(number) - 1

        return str_remove_at(number, found)


if __name__ == "__main__":
    testcases = [
        # (number, digit, correct)
        ("123", "3", "12"),
        ("1231", "1", "231"),
        ("551", "5", "51"),
        ("55552", "2", "5555"),
        ("15454", "4", "1554"),
        ("73197", "7", "7319"),
        ("465725426", "4", "65725426"),
        ("43553327", "3", "4553327"),
        ("3619552534", "5", "361955234"),
    ]
    s = Solution3()

    for number, digit, correct in testcases:
        answer = s.removeDigit(number, digit)
        print(f"({number}, {digit})\t ⟶ {answer}/{correct} {'✅' if answer == correct else '❌'}")

