from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def addTwoNumbers_initial(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    a, b = l1, l2

    head, cur = None, None
    carry = 0
    place = 1

    while (a or b):
        total = place * (carry + (a.val if a else 0) + (b.val if b else 0))
        keep = (total % (place * 10)) // place
        if not head:
            cur = ListNode(keep)
            head = cur
        else:
            cur.next = ListNode(keep)
            cur = cur.next
        carry = total // (place * 10)
        place *= 10
        a = a.next if a else a
        b = b.next if b else b
    
    if (carry):
        cur.next = ListNode(carry)
        
    return head

def addTwoNumbers_solution(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    # Initialise pointers to the heads of each linked list
    a, b = l1, l2

    # Initialise the head of the sum linked list as well as a pointer to its current node
    head, cur = None, None
    # Initialise the carry to 0
    # WHY (here and not in loop)? Because we check it outside the loop
    carry = 0

    # While there are nodes in either linked list...
    while (a or b):
        # Calculate the total of the current place
        total = carry + (a.val if a else 0) + (b.val if b else 0)
        # Calculate the result for the current place and the value to carry over
        keep, carry = total % 10, total // 10

        # If there is no head yet, start a linked list at cur and update head
        if not head:
            cur = ListNode(keep)
            head = cur
        # Else, update cur.next then cur
        else:
            cur.next = ListNode(keep)
            cur = cur.next
    
        # Update a and b if possible
        a = a.next if a else a
        b = b.next if b else b
    
    # Take care of any remainder
    if (carry):
        cur.next = ListNode(carry)
    
    # Return the head of the sum linked list
    return head


# Based on solution at https://leetcode.com/problems/add-two-numbers/solutions/5378155/video-simple-addition-algorithm-python-javascript-java-and-c
# Changed variable names for my ease of understanding
def addTwoNumbers_optimal(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
    cur = ListNode()
    sentinel = cur

    total = carry = 0

    while l1 or l2 or carry:
        total = carry

        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        
        num = total % 10
        carry = total // 10
        cur.next = ListNode(num)
        cur = cur.next
    
    return sentinel.next