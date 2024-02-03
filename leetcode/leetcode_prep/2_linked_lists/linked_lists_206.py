from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # If list is empty or has has one element, return list
    if not head:
        return head
    if not head.next:
        return head

    # Keep track of the previous, current and next nodes
    cur, prev= head, None
    next = cur.next
    setNewTail = False
    while next:
        # Move the pointers for the previous and current forward
        prev, cur = cur, next

        # If the initial next has a next, update so it points to that
        next = cur.next if cur.next else None

        # Make current point to previous
        cur.next = prev

        # If this was the head and this has not been done before, set the previous's next to None
        if (prev.val == head.val) and (not setNewTail):
            prev.next = None
            setNewTail = True
    
    # Return the linked list
    return cur

def reverseList_optimal(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = None
    while head:
        var = head.next
        head.next = dummy
        dummy = head
        head = var
    
    return dummy
