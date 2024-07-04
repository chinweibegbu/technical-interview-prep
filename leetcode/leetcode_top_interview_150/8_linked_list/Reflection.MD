# Solution Reflections
**Reflection Guide**:
* "*Initial Approach*" covers my initial approach(es)
* "*Solution Approach*" covers the approach I used that was accepted by all Leetcode testcases
* "*Optimal Approach*" covers an approach I saw in the submissions which I deemed to be more intuitive or easier than mine
* A single asterisk (*) by a point is used to indicate that an analysis as based on a Google search
* A double question mark (??) by a point is used to indicate a lack of trust in my personal analysis
* --:--:-- in the time slot means that I couldn't solve it on my own
* 00:00:00 in the time slot means that I had already solved it before doing the Leetcode 150

## Linked List Problems

### 141 Linked List Cycle
⌛00:00:00 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-interview-150)

* Solution Approach: → **O(n)**, **O(n)**
  * **IDEA**: Keep track of nodes using a dictionary and return True if we encounter a node already in the dictionary.
* Optimal Approach: → **O(n)**, **O(1)**
  * **IDEA**: Use slow and faster pointers, where fast moves two times as fast as slow. Return True if slow and fast are ever the same

**THOUGHTS**: I thought about my solution approach from teh last time instantaneously. I completely forgot about the slow-fast pointer approach (I think this was influenced by the fact that I never did and still do not understand why slow and fast are determined to meet each other if there is a cycle). >>> See previous reflection for question #141 in `../../leetcode_prep/2_linked_lists/Reflection.MD`.

### #2 Add Two Numbers
⌛26:06:43 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150)

* Initial Approach
* Initial Approach: → **O(n)**, **O(1)**
  * **IDEA**: Iterate through the linked lists and built the result linked list in the same pass
  * **ALGORITHM**:
    1. Initialise pointers to the heads of each linked list, a and b
    2. Initialise the head of the resulting linked list as well as a pointer to its current node
    3. Initialise carry to 0
    4. While there are nodes in either linked list:
       1. Calculate the total of the current place
       2. Calculate the value for the current place and the value to carry over
       3. If there is no head yet, start a linked list with the value for the current place at cur and update head
       4. Else, set cur's next to the value for the current place and update cur to point to its next
       5. Update a and b to their nexts is possible
    5. If there is a non-zero value in carry after we've gone through both linked lists, add that to the resulting linked list
    6. Return the head of the resulting linked list
* Solution Approach
  * **IDEA**: Same as Initial Approach but removed the need to keep track of the current place
  * Improvements:
    * Same space complextity but reduces the number of variables used
* Optimal Approach: → **O(n)**, **O(1)**
  * **IDEA**: Same as Solution Approach but more streamlined
  * Improvement:
    * Same space complextity but reduces the number of variables used
    <br>**THOUGHTS**: I think that, with the approach used, the variable naming should be different as "carry" now holds more than "carry" at some points. This is the reason I decided to leave my variable naming (to improve readiability without additional space complexity cost).

**THOUGHTS**:
* I have apparently tried to solve this problem before. I wonder why I couldn't. I feel there is a similar problem I am forgetting which I was able to solve and then it was this one I was having issues with. Hmm...
* Glad that my solution does everything in one pass so it is both O(n) in actuality and complexity.

### #21 Merge Two Sorted Lists
⌛00:00:00 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/merge-two-sorted-lists/description/?envType=study-plan-v2&envId=top-interview-150)

* Solution Approach: → **O(n)**, **O(n)**
  * **IDEA**: Use pointers and update the pointers based on which of them is currently less then add the lesser to the resulting linked list. Return the head of the resulting linked list.

**THOUGHTS**: See previous code for question #21 in `../../leetcode_prep/8_recursion/recursion_21.py` and its reflection in `../../leetcode_prep/8_recursion/Reflection.MD`.

### #92 Reverse Linked List II
⌛14:28:47 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=study-plan-v2&envId=top-interview-150)

* Solution Approach: → **O(n)**, **O(n)**
  * **IDEA**: Copy elements to reverse and overwrite nodes with copied elements in reverse order
  * **ALGORITHM**:
    1. Initialise iterator, cur, to head
    2. Initialise position variable, pos, to 1 
    <br>**WHY?** Because left and right are both one-indexed, NOT zero-indexed
    3. Initialise a variable to store a reference to the left node
    <br>**WHY?** So that, when replacing the values in the portion to reverse, we don't have to start from the beginning of the linked list again (remember that we only have a reference to head)
    4. Initialise an array to store the values to reverse
    5. While pos is less than or equal to right:
       1. If pos is greater than or equal to left, add cur's val to the array
       2. If pos is equal to left, store a reference to it in the variable initialised in step #3
       <br>**NOTE**: "or equal to" in included for the conditions because we also reverse the nodes at those positions
       3. Update cur by pointing it to its next
       4. Update pos by incrementing it by 1
    6. Set cur to the variable initialied in step #3 and updated in step #5 #2
    7. For i in the backwards range of values:
       1. Overwrite cur's val with the current value in the array
       2. Update cur by pointing to its next
    8. Return head
* Optimal Approach: → **O(n)**, **O(1)**
  * Based on [explanation and code by Neetcode](https://youtu.be/RF_M9tX4Eag)
  * **ALGORITHM**:
    1. Create a dummy node pointint to the head
    2. Get a pointer to the left position while keeping track of a prev and cur
    3. Reverse the target portion of the list, using a new prev pointer
    4. Point left's next (which is original prev's next's next) to cur
    <br>**WHY?** Because, at this point, cur will be pointing to the elemnt beside right
    5. Point original prev's next to prev
    <br>**WHY?** Because, at this point, prev will be pointing to right
    6. Return dummy's next instead of head 
    <br>**WHY?** Because the references could have changed in the process above
  * Improvements:
    * Runs in the same time complexity but with only one pass (my Solution Approach uses two)
  * **CODE**:
    ![Neetcode's solution code for leetcode #92](../images/neetcode_11_comment.png)

**NOTE**: I implemented the code in reverseBetween_optimal() on my own based on my understanding but needed help with the last two lines so I cannot say I did it all on my own

## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/