from collections import deque

class MyStack:

    def __init__(self):
        self.main = deque()
        self.holder = deque()
        self.size = 0

    def push(self, x: int) -> None:
        # Add elements
        self.main.appendleft(x)

        # Increment size by 1
        self.size += 1

    def pop(self) -> int:
        # Move elements to holder
        counter = self.size
        while counter > 0:
            self.holder.appendleft(self.main.pop())
            counter -= 1

        # Decrement size by 1
        self.size -= 1
        
        # Move elements back to main
        counter = self.size
        while counter > 0:
            self.main.appendleft(self.holder.pop())
            counter -= 1

        # Return the only elements left in holder
        return self.holder.pop()

    def top(self) -> int:
        # Move elements to holder
        counter = self.size
        while counter > 0:
            popped = self.main.pop()
            self.holder.appendleft(popped)
            counter -= 1
        
        # Move elements back to main
        counter = self.size
        while counter > 0:
            self.main.appendleft(self.holder.pop())
            counter -= 1

        # Return the last popped element 
        return popped

    def empty(self) -> bool:
        return self.size == 0

class MyStack_OneQueue:

    def __init__(self):
        self.queue = deque()
        self.size = 0

    def push(self, x: int) -> None:
        # Add elements
        self.queue.appendleft(x)

        # Increment size by 1
        self.size += 1

    def pop(self) -> int:
        # Remove all but one element and add to back of queue
        counter = self.size
        while counter > 1:
            self.queue.appendleft(self.queue.pop())
            counter -= 1

        # Decrement size by 1
        self.size -= 1

        # Return the only element not moved to back of queue a.k.a. LAST IN
        return self.queue.pop()

    def top(self) -> int:
        # Remove all elements and add to back of queue
        counter = self.size
        while counter > 0:
            # REMEMBER: Keep track of the last popped element 
            popped = self.queue.pop()
            self.queue.appendleft(popped)
            counter -= 1

        # Return the last popped element a.k.a. LAST IN
        return popped

    def empty(self) -> bool:
        return self.size == 0

class MyStack_OneQueue_Optimal:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        # Add elements
        self.queue.appendleft(x)

    def pop(self) -> int:
        # Remove all but one element and add to back of queue
        for i in range(1, len(self.queue)):
            self.queue.appendleft(self.queue.pop())

        # Return the only element not moved to back of queue a.k.a. LAST IN
        return self.queue.pop()

    def top(self) -> int:
        # Remove all elements and add to back of queue
        for i in range(len(self.queue)):
            # REMEMBER: Keep track of the last popped element 
            popped = self.queue.pop()
            self.queue.appendleft(popped)

        # Return the last popped element a.k.a. LAST IN
        return popped

    def empty(self) -> bool:
        return len(self.queue) == 0
        