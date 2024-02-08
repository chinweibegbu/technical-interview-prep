class MyHashSet_Initial:

    def __init__(self):
        self.hash_set = []

    def add(self, key: int) -> None:
        # Add key to hashset if it isn't already there
        if not (key in self.hash_set):
            self.hash_set.append(key)

    def remove(self, key: int) -> None:
        # Remove key from hashset if it is there
        if (key in self.hash_set):
            self.hash_set.remove(key)

    def contains(self, key: int) -> bool:
        # Use the `in` operator to check whether the hashset has the key
        return (key in self.hash_set)

class LinkedListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet_WithHashing:

    def __init__(self):
        self._MAXLEN = 100
        self.hash_set = [None] * self._MAXLEN

    def add(self, key: int) -> None:
        # Add key to hashset if it isn't already there
        if not(self.contains(key)):
            # Get linked list storing key
            index = key % self._MAXLEN
            cur = self.hash_set[index]
            
            # If the slot has a node, add the key to the end of the linked list 
            if (cur):
                while (cur.next):
                    cur = cur.next
                cur.next = LinkedListNode(key)
            # Else, fill the slot with a node
            else:
                self.hash_set[index] = LinkedListNode(key)

    def remove(self, key: int) -> None:
        # Add key to hashset if it isn't already there
        if (self.contains(key)):
            # Get linked list storing key
            index = key % self._MAXLEN
            cur = self.hash_set[index]

            # Delete the node with val of key
            # If key is in head node, point array slot to its next
            if (cur.val == key):
                self.hash_set[index] = cur.next
            # Else, iterate until you find key and connect its prev to its next
            else:
                prev = None
                while (cur):
                    if (cur.val == key):
                        prev.next = cur.next
                        break
                    prev, cur = cur, cur.next

    def contains(self, key: int) -> bool:
        # Get linked list potentially storing key
        index = key % self._MAXLEN
        cur = self.hash_set[index]   

        # Iterate through linked list until key is found OR end is reached
        while (cur):
            if (cur.val == key):
                return True
            cur = cur.next
        return False

class MyHashSet_WithHashing_Optimised:

    def __init__(self):
        self._MAXLEN = 100
        self.hash_set = [None] * self._MAXLEN

    def add(self, key: int) -> None:
        # Get linked list storing key
        index = key % self._MAXLEN
        cur = self.hash_set[index]
        
        # If the slot has a node, add the key to the end of the linked list 
        if (cur):
            prev = None
            while (cur):
                # If the value is already in the linked list, return
                if (cur.val == key):
                    return
                prev, cur = cur, cur.next
            prev.next = LinkedListNode(key)
        # Else, fill the slot with a node
        else:
            self.hash_set[index] = LinkedListNode(key)

    def remove(self, key: int) -> None:
        # Get linked list storing key
        index = key % self._MAXLEN
        cur = self.hash_set[index]

        # If there is no linked list at the slot, return
        if (not cur):
            return

        # Delete the node with val of key
        # If key is in head node, point array slot to its next
        if (cur.val == key):
            self.hash_set[index] = cur.next
        # Else, iterate until you find key and connect its prev to its next
        else:
            prev = None
            while (cur):
                if (cur.val == key):
                    prev.next = cur.next
                    break
                prev, cur = cur, cur.next

    def contains(self, key: int) -> bool:
        # Get linked list potentially storing key
        index = key % self._MAXLEN
        cur = self.hash_set[index]   

        # Iterate through linked list until key is found OR end is reached
        while (cur):
            if (cur.val == key):
                return True
            cur = cur.next
        return False
    