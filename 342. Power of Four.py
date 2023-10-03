class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        while True:
            if n % 4 == 0:
                n /= 4
            else:
                return False
            if n == 1:
                return True
