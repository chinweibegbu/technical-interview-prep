from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
    # Edge case #1: Empty list
    if not head:
        return None
    
    # Continue until the end of the list
    prev, cur = None, head
    while cur:
        if (cur.val == val):
            # Edge case #2: cur is head and needs to be deleted
            if (cur == head):
                # Update head to point to its .next
                head = head.next
                # Point cur to the updated head
                cur = head
            else:
                # Skip cur
                prev.next = cur.next
                # Update cur to next element
                cur = cur.next
        else:
            prev, cur = cur, cur.next
    
    # Return new head (it may or may not have changed)
    return head