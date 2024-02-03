from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # Initialise slow and fast to head
    slow, fast = head, head

    # While fast is not None or it's .next is not None, continue
    while ((fast is not None) and (fast.next is not None)):
        slow = slow.next
        fast = fast.next.next

    # Return slow
    return slow