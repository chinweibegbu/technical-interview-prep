from collections import deque

class MinStack_solution:

    def __init__(self):
        self.stack = deque([])
        self.minimums = deque([])

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (len(self.minimums) == 0) or (val < self.minimums[-1]):
            self.minimums.append(val)
        else:
            self.minimums.append(self.minimums[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minimums.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimums[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()