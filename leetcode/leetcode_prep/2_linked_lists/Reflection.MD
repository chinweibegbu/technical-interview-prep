# Solution Reflections
**Reflection Guide**:
* "*Solution Approach*" covers the approach I used that was accepted by all Leetcode testcases while "*Optimal Approach*" covers an approach I saw in the submissions which I deemed to be more intuitive or easier than mine
* A single asterisk (*) by a point is used to indicate that an analysis as based on a Google search
* A double question mark (??) by a point is used to indicate a lack of trust in my personal analysis

## Linked List Problems
### #206 Reverse linked list
⌛01:00:22 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/reverse-linked-list/)

* Solution Approach: Keep track of the previous, current and next nodes. Make swaps and iterate until there is no next node. Return the current node, which is now the head. → **O(n)**
* Optimal Approach: Also uses three pointers but does not use any `if` statements, which seems to contribute poorly to relative performance. See the `reverseList_optimal()` function in `[dsa_with_python\leetcocde\leetcode_prep\2_linked_lists\linked_lists_206.py]` file. The basic algorithm is: Start with prev pointing to None then,
  1. Point next to Head.next
  2. Point Head's .next to prev
  3. Point prev to Head
  4. Point Head to next
    <br> → **O(n)** 

**NOTE**: Insert image of visualisation of the optimal approach's code <br>
**NOTE**: After coming up with an algorithm, always visualise on paper before coding

### #876 Middle of linked list
⌛10:51:82 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/middle-of-the-linked-list/)

* Solution Approach: Initilise both pointers to head. Use a slow and fast pointer with the fast pointer moving twice as fast as the slow pointer. Return the slow pointer when the fast pointer or its .next is None → **O(n)**

**NOTE**: Remember to talk out loud and consider edge cases

### #141 Linked list cycle
⌛07:07:23 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/linked-list-cycle/)

* Solution Approach: Use a dictionary to keep track of visited nodes. Parse until (A) you visit an already-visited node or (B) you reach the end of the linked list (B). If (A), there is a cycle so return True. If (B), there is no cycle so return False. → **O(n)**
* Optimal Approach: Use slow and fast pointers. Parse until (A) slow and fast are the same or (B) fast or fast's next is None. If (A), there is a cycle so return True. If (B), there is no cycle so return False → **O(n)** *

**NOTE:** The approach above is less an optimal approach than it is an alternative approach. It came to mind as another way to implement the solution, as I am aware this approach is common. However, I did not use it because, one, I cannot explain why the two pointers are guaranteed to meet with discrete steps (I say this because the runner or "tortoise-hare" analogy uses a continuous distance which I do not think is applicable). Two, because of the reason above, I am unable to figure out the time complexity. 

### #1290 Convert binary number in a linked list to integer
⌛00:00:00 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/)

* Initial Approach: Content → **O(n<sup>2</sup>)** ??
* Solution Approach: Content → **O(n)**
* Optimal Approach: Content → **O(n)** *

### #203 Removed linked list elements
⌛00:00:00 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/remove-linked-list-elements/)

* Initial Approach: Content → **O(n<sup>2</sup>)** ??
* Solution Approach: Content → **O(n)**
* Optimal Approach: Content → **O(n)** *

## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/