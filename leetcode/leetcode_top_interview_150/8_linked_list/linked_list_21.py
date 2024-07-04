from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Based on my original solution from `../../leetcode_prep/8_recursion/resursion_21.py`
# Changed "newHead" to "sentinel" to improve variable naming and code readability
def mergeTwoLists_solution(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # Create new head to return and new tail to make insertion O(1)
    sentinel = ListNode()
    newTail = sentinel
    
    # Add elements from both lists and update the pointer until either of the lists is empty
    while (list1 and list2):
        if (list1.val <= list2.val):
            newTail.next = ListNode(list1.val)
            list1, newTail = list1.next, newTail.next
        else:
            newTail.next = ListNode(list2.val)
            list2, newTail = list2.next, newTail.next
            
    # Set the end of the list with remnants to the new list
    newTail.next = list1 if list1 else list2
    
    # Return the new list without the "null head" a.k.a. sentinel
    return sentinel.next