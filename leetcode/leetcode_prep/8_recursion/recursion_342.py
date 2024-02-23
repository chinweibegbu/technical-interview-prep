class Solution_Initial_1:
    def isPowerOfFour(self, n: int) -> bool:
        if (n <= 0): return False

        for x in range(0, 31):
            if (x % 2 != 0): 
                continue
            if (2**x == n): 
                return True
        
        return False
    
class Solution_Initial_2:
    def isPowerOfFour(self, n: int) -> bool:
        for x in range(0, 31):
            if (x % 2 != 0): 
                continue
            if (2**x == n): 
                return True

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for x in range(0, 31):
            if (2**x == n):
                return (x%2 == 0)

class Solution_Alternative:
    def isPowerOfFour(self, n: int) -> bool:
        if (n == 1) :
            return True
        elif (n < 1):
            return False
        return self.isPowerOfFour(n/4)