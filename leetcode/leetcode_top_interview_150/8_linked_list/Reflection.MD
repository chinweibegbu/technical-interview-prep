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

## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/