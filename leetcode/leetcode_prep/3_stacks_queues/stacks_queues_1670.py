class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []
        self.count = 0

    def pushFront(self, val: int) -> None:
        # Add a list containing the new value to the existing list
        self.queue = [val] + self.queue
        self.count += 1

    def pushMiddle(self, val: int) -> None:
        # Add a list with the first list half to a list with the new value to a list with the rest of the elements
        middle = int((self.count) / 2 if (self.count%2==0) else (self.count-1) / 2)
        self.queue = self.queue[:middle] + [val] + self.queue[middle:]
        self.count += 1

    def pushBack(self, val: int) -> None:
        # Add item to back of list with the in-built function
        self.queue.append(val)
        self.count += 1

    def popFront(self) -> int:
        # Edge case: Queue is empty
        if (self.count == 0):
            return -1

        # Get the first/front element with indexing then alter the queue with splitting
        front = self.queue[0]
        self.queue = self.queue[1:]
        self.count -= 1
        return front

    def popMiddle(self) -> int:
        # Edge case: Queue is empty
        if (self.count == 0):
            return -1

        # Get the middle element then alter the queue with list splitting and adding
        middle = int(((self.count) / 2)-1 if (self.count%2==0) else (self.count-1) / 2)
        middle_element = self.queue[middle]
        self.queue = self.queue[:middle] + self.queue[middle+1:]
        self.count -= 1
        return middle_element


    def popBack(self) -> int:
        # Edge case: Queue is empty
        if (self.count == 0):
            return -1

        # Get the last element with indexing then alter the queue with splitting
        back = self.queue[-1]
        self.queue = self.queue[:int(self.count-1)]
        self.count -= 1
        return back

class FrontMiddleBackQueue_InBuiltFunctions:

    def __init__(self):
        self.queue = []
        self.count = 0

    def pushFront(self, val: int) -> None:
        # Add new element at beginning
        self.queue.insert(0, val)
        self.count += 1

    def pushMiddle(self, val: int) -> None:
        # Add new element at middle index
        middle = int((self.count) / 2 if (self.count%2==0) else (self.count-1) / 2)
        self.queue.insert(middle, val)
        self.count += 1

    def pushBack(self, val: int) -> None:
        # Add new element to back of list
        self.queue.append(val)
        self.count += 1

    def popFront(self) -> int:
        # Edge case: Queue is empty
        if (self.count == 0):
            return -1

        # Get front element, decrement count and return
        front = self.queue.pop(0)
        self.count -= 1
        return front

    def popMiddle(self) -> int:
        # Edge case: Queue is empty
        if (self.count == 0):
            return -1

        # Get middle element, decrement count and return
        middle = int(((self.count) / 2)-1 if (self.count%2==0) else (self.count-1) / 2)
        middle_element = self.queue.pop(middle)
        self.count -= 1
        return middle_element


    def popBack(self) -> int:
        # Edge case: Queue is empty
        if (self.count == 0):
            return -1

        # Get back element, decrement count and return
        back = self.queue.pop()
        self.count -= 1
        return back
        
class FrontMiddleBackQueue_Optimal:

    def __init__(self):
        self.queue = []

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        length = len(self.queue)
        self.queue.insert(length//2, val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        if not self.queue:
            return -1
        return self.queue.pop(0)
        
    def popMiddle(self) -> int:
        if not self.queue:
            return -1
        length = len(self.queue)
        mid = length // 2
        if length % 2:
            return self.queue.pop(mid)
        else:
            return self.queue.pop(mid - 1)

    def popBack(self) -> int:
        if not self.queue:
            return -1
        return self.queue.pop(-1)
        