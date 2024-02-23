class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Edge case: n is less than or equal to 0
        if (n <= 0):
            return False

        return self.half(n)

    def half(self, n):
        # If you get to 1, i.e. you got to 2 divided by 2, it was a power of 2
        if (n == 1):
            return True
        else:
            # If it cannot be divided by two without a remainder, it is NOT a power of two
            # Else, call the function recursively on half of it
            if (n%2 == 0):
                return self.half(n//2)
            else:
                return False

class Solution_Alternative_Binary:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and bin(n).count('1') == 1

class Solution_Alternative_Constraint:
    def isPowerOfTwo(self, n: int) -> bool:
        for i in range(0, 31):
            if n == (2**i):
                return True