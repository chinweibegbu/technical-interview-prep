class LinkedListNode:
    def __init__(self, pair):
        self.pair = pair
        self.next = None

class MyHashMap:

    def __init__(self):
        self._MAXLEN = 100
        self.hash_map = [None] * self._MAXLEN

    def put(self, key: int, value: int) -> None:
        # Get index and slot content
        index = key % self._MAXLEN
        cur = self.hash_map[index]

        # Continue if there is a linked list in the slot; else, create one 
        if (cur):
            # Parse linked list until second to last node
            prev = None
            while (cur):
                # Update if already in the hashmap
                if (cur.pair[0] == key):
                    cur.pair[1] = value
                    return
                prev, cur = cur, cur.next
            # Insert into the linked list if not there
            prev.next = LinkedListNode([key, value])
        else:
            # Create head node for empty slot
            self.hash_map[index] = LinkedListNode([key, value])

    def get(self, key: int) -> int:
        # Get index and slot content
        index = key % self._MAXLEN
        cur = self.hash_map[index]

        # Parse linked list until the key is found OR end is reached
        while (cur):
            if (cur.pair[0] == key):
                return cur.pair[1]
            cur = cur.next
        # If you reach the end of the linked list OR the loop is never entered, the key is not there
        return -1

    def remove(self, key: int) -> None:
        # Get index and slot content
        index = key % self._MAXLEN
        cur = self.hash_map[index]

        if (cur):
            # If head is to be removed, point slot to its next
            if (cur.pair[0] == key):
                self.hash_map[index] = cur.next
            else:
                # Parse linked list
                prev = None
                while (cur):
                    # Update if already in the hashmap
                    if (cur.pair[0] == key):
                        prev.next = cur.next
                        break
                    prev, cur = cur, cur.next

class MyHashMap_Optimal:

    def __init__(self):
        self.hashmap = {}

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        if (key in self.hashmap.keys()):
            return self.hashmap[key]
        return -1

    def remove(self, key: int) -> None:
        if (key in self.hashmap.keys()):
            self.hashmap.pop(key)
            