from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween_solution(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    cur = head
    pos = 1
    start = None
    values = []
    while pos <= right:
        if (pos >= left):
            values.append(cur.val)
        if (pos == left):
            start = cur
        cur = cur.next
        pos += 1
    cur = start
    for i in range(len(values)-1, -1, -1):
        cur.val = values[i]
        cur = cur.next        
    return head

# Based on Neetcode's explanation at https://youtu.be/RF_M9tX4Eag
def reverseBetween_optimal(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    leftPrev, cur = dummy, head
    for i in range(left-1):
        leftPrev, cur = cur, cur.next
    
    prev = None
    for i in range(right - left + 1):
        tmp = cur.next
        cur.next = prev
        prev, cur = cur, tmp
    
    leftPrev.next.next = cur
    leftPrev.next = prev

    return dummy.next
