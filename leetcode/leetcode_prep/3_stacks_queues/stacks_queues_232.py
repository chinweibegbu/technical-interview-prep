from collections import deque

class MyQueue:

    def __init__(self):
        self.main = deque()
        self.holder = deque()
        self.size = 0

    def push(self, x: int) -> None:
        # Add new element and increment size by 1
        self.main.append(x)
        self.size += 1

    def pop(self) -> int:
        # Edge case: There are no elements
        if (self.size == 0):
            return None

        # Move elements to holder
        counter = self.size
        while (counter > 0):
            self.holder.append(self.main.pop())
            counter -= 1
        
        # Remove and note the top element in holder and decrement size by 1
        popped = self.holder.pop()
        self.size -= 1
        
        # Move elements back to main
        counter = self.size
        while (counter > 0):
            self.main.append(self.holder.pop())
            counter -= 1
            
        # Return the popped element
        return popped

    def peek(self) -> int:
        # Edge case: There are no elements
        if (self.size == 0):
            return None

        # Move elements to holder
        counter = self.size
        while (counter > 0):
            self.holder.append(self.main.pop())
            counter -= 1
        
        # Remove and note the top element in holder then add it to main
        # ALTERNATIVE: Add it back to holder then set counter on Line 57 to self.size, without the -1
        top = self.holder.pop()
        self.main.append(top)
        
        # Move elements back to main
        counter = self.size - 1     # WHY: Because we have already moved the first element back to main
        while (counter > 0):
            self.main.append(self.holder.pop())
            counter -= 1
            
        # Return the peeked element
        return top

    def empty(self) -> bool:
        return self.size == 0


from collections import deque

class MyQueue_Amortised:

    def __init__(self):
        self.main = deque()
        self.holder = deque()
        self.size = 0
        # Initialised such that FIRST IN is at the end
        self.in_main = True

    def push(self, x: int) -> None:
        # If the FIRST IN is not at the end, move elements to back to main
        if not self.in_main:
            counter = self.size
            while counter > 0:
                self.main.append(self.holder.pop())
                counter -= 1
            self.in_main = True

        # Add the newest element to main
        self.main.append(x)
        # Increment size by 1
        self.size += 1

    def pop(self) -> int:
        # Edge case: There are no elements
        if (self.size == 0):
            return None

        # If the FIRST IN is at the end, move elements to holder
        if self.in_main:
            counter = self.size
            while (counter > 0):
                self.holder.append(self.main.pop())
                counter -= 1
            self.in_main = False

        # Pop off the first element in holder a.k.a. LAST IN
        popped = self.holder.pop()
        # Decrement size by 1
        self.size -= 1
        # Return popped off element
        return popped

    def peek(self) -> int:
        # Edge case: There are no elements
        if (self.size == 0):
            return None

        if self.in_main:
            counter = self.size
            while (counter > 0):
                self.holder.append(self.main.pop())
                counter -= 1
            self.in_main = False
            
        # Pop off the first element in holder a.k.a. LAST IN
        # WHY? There is no other way to access said element while using deque
        top = self.holder.pop()
        # Add popped off element back to holder
        self.holder.append(top)
        # Return the saved popped off element
        return top

    def empty(self) -> bool:
        # Return True if size is 0; else, return False
        return self.size == 0

