class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # Edge case: n is less than or equal to 0
        if (n <= 0):
            return False

        # If n is 1, return true
        if (n == 1):
            return True
        else:
            # If n is evenly divisible by three, call recursively on n divided by three
            # Else, return false
            if (n % 3 == 0):
                return self.isPowerOfThree(n//3)
            else:
                return False