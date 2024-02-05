from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        # If the stack is empty, just put val as the min
        if (len(self.stack) == 0):
            self.stack.append((val, val))
        else:
            # Get the current min
            minimum = self.getMin()

            # Insert tuple into stack with min based on comparison
            if (val < minimum):
                self.stack.append((val, val))
            else:
                self.stack.append((val, minimum))

    def pop(self) -> None:
        # Return the value of the top element tuple
        return self.stack.pop()[0]

    def top(self) -> int:
        # Remove and note the top element
        popped = self.stack.pop()
        # Add it back to the stack
        self.stack.append(popped)
        
        # Return the value of the popped element tuple
        return popped[0]

    def getMin(self) -> int:
        # Remove and note the top element
        popped = self.stack.pop()
        # Add it back to the stack
        self.stack.append(popped)
        
        # Return the minimum of the popped element tuple
        return popped[1]
