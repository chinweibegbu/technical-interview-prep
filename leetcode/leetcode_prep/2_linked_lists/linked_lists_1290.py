from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(self, head: ListNode) -> int:
    # Parse once to get number of elements
    cur, count = head, -1
    while cur:
        count += 1
        cur = cur.next

    # Parse a second time to return the total
    cur, total = head, 0
    while cur:
        total += (cur.val * (2**count))
        cur = cur.next
        count -= 1

    return total
        