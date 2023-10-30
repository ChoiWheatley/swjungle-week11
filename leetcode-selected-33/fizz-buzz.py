from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        50ms 17.35MB
        """
        ret = [str(i) for i in range(1, n + 1)]
        for time in range(1, n // 3 + 1):
            idx = time * 3 - 1
            ret[idx] = "Fizz"

        for time in range(1, n // 5 + 1):
            idx = time * 5 - 1
            ret[idx] = "Buzz"

        for time in range(1, n // 15 + 1):
            idx = time * 15 - 1
            ret[idx] = "FizzBuzz"

        return ret


class Solution2:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        54ms 17.16MB
        """
        ret = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                ret.append("FizzBuzz")
            elif i % 5 == 0:
                ret.append("Buzz")
            elif i % 3 == 0:
                ret.append("Fizz")
            else:
                ret.append(str(i))
        return ret


class Solution3:
    def fizzBuzz(self, n: int) -> List[str]:
        ret = [""] * n
        for time in range(1, n // 3 + 1):
            idx = time * 3 - 1
            ret[idx] = "Fizz"

        for time in range(1, n // 5 + 1):
            idx = time * 5 - 1
            ret[idx] = "Buzz"

        for time in range(1, n // 15 + 1):
            idx = time * 15 - 1
            ret[idx] = "FizzBuzz"

        return ret
