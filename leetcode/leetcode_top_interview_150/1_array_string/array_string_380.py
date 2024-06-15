from operator import delitem
from random import randint, choice

class RandomizedSet_FAILED:

    def __init__(self):
        self.SIZE = 10**5
        self.MAX_SIZE = (2 * self.SIZE) + 1
        self.arr = [None] * self.MAX_SIZE
        self.elements = {}

    def insert(self, val: int) -> bool:
        # Get hash
        index = self.getHash(val)

        # Update non-empty indices tracker
        self.elements[val] = True

        # Edge case: val is 0
        if (index == (self.SIZE+1)):
            if (self.arr[index] == None):
                self.arr[index] = 0
                return True
            else:
                return False
        else:
            # Create LinkedList at index OR insert into existing LinkedList
            if (self.arr[index]):
                return self.arr[index].insert(val)
            else:
                self.arr[index] = LinkedList(val)
                return True

    def remove(self, val: int) -> bool:
        # Get hash
        index = self.getHash(val)

        # Edge case: val is 0
        result = False
        initialLength = None
        if (index == (self.SIZE+1)):
            if (self.arr[index] == None):
                result = False
            else:
                self.arr[index] = None
                result = True
        else:
            # Return the result of trying to remove a node from the LinkedList there
            if (self.arr[index]):
                initialLength = self.arr[index].length
                result = self.arr[index].remove(val)
            else:
                result = False
        
        if (result and ((val == 0) or (initialLength == 1))):
            # Update non-empty indices tracker
            delitem(self.elements, val)

        return result

    def getRandom(self) -> int:
        return list(self.elements.keys())[randint(0, len(self.elements)-1)]
        # numNonEmptyIndices = len(self.hasElements.keys())
        # randomindexOfNonEmptyIndex = randint(0,numNonEmptyIndices-1)
        # r = list(self.hasElements.keys())[randomindexOfNonEmptyIndex]

        # if (r == (self.SIZE+1)):
        #     return 0
        # else:
        #     linked_list_len = self.arr[r].length
        #     random_index = randint(0, linked_list_len-1)
        #     return self.arr[r].fetch(random_index)
    
    def getHash(self, val: int) -> int:
        if (val < 0):
            return (val % self.SIZE)
        elif (val > 0):
            return (val % self.SIZE) + (self.SIZE)
        else:
            return self.SIZE + 1
        
class LinkedListNode:

    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self, val: int):
        self.head = LinkedListNode(val)
        self.length = 1

    def insert(self, val: int) -> bool:
        prev, cur = None, self.head
        
        while cur:
            if (cur.val == val):
                return False
            prev, cur = cur, cur.next
        
        prev.next = LinkedListNode(val)
        self.length += 1
        return True

    def remove(self, val: int) -> bool:
        # Edge case: Head is to be deleted
        if (self.head.val == val):
            self.head = self.head.next
            self.length -= 1
            return True

        prev, cur = None, self.head

        while cur:
            if (cur.val == val):
                prev.next = cur.next
                self.length -= 1
                return True
            prev, cur = cur, cur.next
        
        return False
    
    def fetch(self, position: int) -> int:
        cur = self.head
        for i in range(position):
            cur = cur.next
        return cur.val

class RandomizedSet_solution_1:
    def __init__(self):
        self.elements = {}

    def insert(self, val: int) -> bool:
        if (val in self.elements.keys()):
            return False
        else:
            self.elements[val] = True
            return True        

    def remove(self, val: int) -> bool:
        if (val in self.elements.keys()):
            delitem(self.elements, val)
            return True
        else:
            return False 

    def getRandom(self) -> int:
        r = randint(0, (len(self.elements.keys())-1))
        return list(self.elements.keys())[r]

class RandomizedSet_solution_2:

    def __init__(self):
        self.elements = {}

    def insert(self, val: int) -> bool:
        var = self.elements.get(val, None)
        if var:
            return False
        else:
            self.elements[val] = True
            return True        

    def remove(self, val: int) -> bool:
        var = self.elements.get(val, None)
        if (var):
            delitem(self.elements, val)
            return True
        else:
            return False 

    def getRandom(self) -> int:
        r = randint(0, (len(self.elements.keys())-1))
        return list(self.elements.keys())[r]

# Based on solution at https://leetcode.com/problems/insert-delete-getrandom-o1/solutions/4572728/beats-99-84-users-c-java-python-javascript-explained
# Changed variable names and added comments for my ease of understanding
class RandomizedSet_optimal:
    def __init__(self):
        # SPACE: O(n)
        self.elements = []
        self.indices = {}

    def search(self, val):
        return val in self.indices

    def insert(self, val):
        if self.search(val):
            return False

        self.elements.append(val)
        self.indices[val] = len(self.elements) - 1
        return True

    def remove(self, val):
        if not self.search(val):
            return False

        # Get the index of val
        idx = self.indices[val]
        # Replace it with the element at the end
        self.elements[idx] = self.elements[-1]
        # Update the index of former last element to the index we just moved it to
        self.indices[self.elements[-1]] = idx
        # Remove the now unnecessary duplicate element at the end of the array
        self.elements.pop()
        # Delete val (which is no longer in the element list) from the indices map
        del self.indices[val]
        
        return True

    def getRandom(self):
        return choice(self.elements)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()