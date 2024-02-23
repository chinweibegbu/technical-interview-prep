class Solution:
    def fib(self, n: int) -> int:
        if ((n == 0) or (n == 1)): 
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
        
class Solution_Optimal:
    def fib(self, n: int) -> int:
        cache = {
            0: 0,
            1: 1
        }
        
        def fibonacci(N):
            if N in cache:
                return cache[N]

            result = fibonacci(N-1)+ fibonacci(N-2)
            cache[N] = result
            return result

        return fibonacci(n)
            