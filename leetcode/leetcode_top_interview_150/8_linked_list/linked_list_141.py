from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle_solution(head: Optional[ListNode]) -> bool:
    # Initialise visited tracker and current node, cur
    visited = {}
    cur = head

    # Parse the linked list until a node is repeated OR cur is None
    while (cur):
        # If cur is in visited, there is a cycle
        if cur in visited: 
            return True
        visited[cur] = True
        cur = cur.next
    
    # If you get to this point, there is no cycle
    # WHY? Because there is no way to exit the while loop should one exist
    return False

def hasCycle_optimal(head: Optional[ListNode]) -> bool:
    # Create a slow and a fast pointer
    slow, fast = head, head
    
    # Parse the linked list until a slow and fast are the same OR fast/fast.next is None
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # If slow and fast are the same, there is a cycle
        if slow is fast:
            return True
        
    # If you get to this point, there is no cycle
    return False