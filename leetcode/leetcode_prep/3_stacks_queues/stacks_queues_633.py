class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None]*k
        self.size = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        # Edge case: Queue is full
        if (self.isFull()):
            return False

        # Iterate from front to rear of queue
        cur = self.front
        for i in range(self.size):
            # If current slot if empty, add new value and update rear pointer
            if (self.queue[cur] is None):
                self.queue[cur] = value
                self.rear = cur
                return True
            # Update cur in a cyclical manner
            cur = (cur + 1) % self.size
        
    def deQueue(self) -> bool:
        # Edge case: Queue is empty
        if (self.isEmpty()):
            return False
        
        # Empty front slot of queue
        self.queue[self.front] = None

        # Update front pointer in a cyclical manner (IF there is any other element in the list)
        next_pointer = (self.front + 1) % self.size
        if (self.queue[next_pointer] is not None):
            self.front = next_pointer
        
        # Return True on success
        return True

    def Front(self) -> int:
        # Edge case: Queue is empty
        if (self.isEmpty()):
            return -1

        return self.queue[self.front]

    def Rear(self) -> int:
        # Edge case: Queue is empty
        if (self.isEmpty()):
            return -1
        
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        first_slot = self.queue[self.front]
        last_slot = self.queue[(self.front + (self.size-1))%self.size]
        return (first_slot is None) and (last_slot is None)

    def isFull(self) -> bool:
        first_slot = self.queue[self.front]
        last_slot = self.queue[(self.front + (self.size-1))%self.size]
        return (first_slot is not None) and (last_slot is not None)

class MyCircularQueue_Optimal:

    def __init__(self, k: int):
        self.queue = [None]*k
        self.size = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        # Edge case: Queue is full
        if (self.isFull()):
            return False

        # Insert behind the rear pointer if rear is occupied. Else, insert at rear pointer
        if (self.queue[self.rear] is not None):
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        
        return True
        
    def deQueue(self) -> bool:
        # Edge case: Queue is empty
        if (self.isEmpty()):
            return False
        
        # Empty front slot of queue
        self.queue[self.front] = None

        # Update front pointer in a cyclical manner (IF there is any other element in the list)
        next_pointer = (self.front + 1) % self.size
        if (self.queue[next_pointer] is not None):
            self.front = next_pointer
        
        # Return True on success
        return True

    def Front(self) -> int:
        # Edge case: Queue is empty
        if (self.isEmpty()):
            return -1

        return self.queue[self.front]

    def Rear(self) -> int:
        # Edge case: Queue is empty
        if (self.isEmpty()):
            return -1
        
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        first_slot = self.queue[self.front]
        last_slot = self.queue[(self.front + (self.size-1))%self.size]
        return (first_slot is None) and (last_slot is None)

    def isFull(self) -> bool:
        first_slot = self.queue[self.front]
        last_slot = self.queue[(self.front + (self.size-1))%self.size]
        return (first_slot is not None) and (last_slot is not None)
