from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution_Initial_1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # If both lists are empty or list2 is empty, return list1
        if (((list1) and (not list2)) or ((not list1) and (not list2))):
            return list1
        # If list1 is empty, return list2
        elif ((not list1) and (list2)):
            return list2
        else:
            # Compare the two non-empty lists and create a new head
            # REMEMBER: Update the list whose head is the newHead
            newHead = None
            if (list1.val <= list2.val):
                newHead = ListNode(list1.val)
                list1 = list1.next
            else:
                newHead = ListNode(list2.val)
                list2 = list2.next
                
            # Add elements from both lists and update the pointer until either of the lists is empty
            newTail = newHead
            while (list1 and list2):
                if (list1.val <= list2.val):
                    newTail.next = ListNode(list1.val)
                    list1, newTail = list1.next, newTail.next
                else:
                    newTail.next = ListNode(list2.val)
                    list2, newTail = list2.next, newTail.next
            # Set the end of the list with remnants to the new list
            newTail.next = list1 if list1 else list2
            
            # Return the new list
            return newHead

class Solution_Initial_2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # If both lists are empty or list2 is empty, return list1
        if (((list1) and (not list2)) or ((not list1) and (not list2))):
            return list1
        # If list1 is empty, return list2
        elif ((not list1) and (list2)):
            return list2
        else:
            # Create new head to return and new tail to make insertion O(1)
            newHead = ListNode()
            newTail = newHead
            
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
            
            # Return the new list without the "null head"
            return newHead.next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create new head to return and new tail to make insertion O(1)
        newHead = ListNode()
        newTail = newHead
        
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
        
        # Return the new list without the "null head"
        return newHead.next