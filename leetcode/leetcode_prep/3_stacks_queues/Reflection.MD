# Solution Reflections
**Reflection Guide**:
* "*Initial Approach*" covers my initial approach(es)
* "*Solution Approach*" covers the approach I used that was accepted by all Leetcode testcases
* "*Optimal Approach*" covers an approach I saw in the submissions which I deemed to be more intuitive or easier than mine
* A single asterisk (*) by a point is used to indicate that an analysis as based on a Google search
* A double question mark (??) by a point is used to indicate a lack of trust in my personal analysis

## Stack & Queue Problems

### #232 Implement queue using stacks
⌛09:57:07 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/implement-queue-using-stacks/)

* Initial Approach:
  * This was a massive flop (⌛29:47:25 and still only passing 11 out of 22 test cases)
  * I felt like I knew what to do. I am pretty certain that I have already implemented it, in fact.
  * Approaches:
    * Use two `deque`s --> **PROBLEM**: I could not remember the in-built functions for this off the top of my head. Did not work at all.
    * Use two lists --> **PROBLEM**: Again, I could not remember the in-built functions for this off the top of my head. Even when I started calling the correct in-buolt functions, I only passes 11 out of 22 test cases and I could not figure out why. 
  * Predicted function runtimes (assuming the space for the two "stacks" does not count):
     *  `push()`: **O(1)**, **O(1)**
     *  `pop()`: **O(n)**, **O(1)**
     *  `peek()`: **O(n)**, **O(1)**
     *  `empty()`: **O(1)**, **O(1)**
* Solution Approach: Literally my initial approach with the `deque`s; maybe I was just stressed and anxious and making silly mistakes the first time. I added a size marker though because `deque` does not have a `size` property or `isEmpty()` function so I have to track it on my own.
* Solution Approach (Amortised): Same as the above approach but track whether the elements are in the main or helper stack/`deque`. The difference is in the number of times you need to move items back and forth between the two stacks. 
     *  `push()`: If NOT in main, move elements back to main. Add new element and increment size.
     *  `pop()`: If in main, move elements to holder. Remove and return the first element in holder (a.k.a. LAST IN).
     *  `peek()`: If in main, move elements to holder. Remove and save the first element in holder (a.k.a. LAST IN). Add it back to holder and return the saved removed element.
     *  `empty()`: Return if size if zero or not
* Optimal Approach (Amortised): Same as the above but do not create a variable to track where the elements are - instead, just check the if main or holder are empty. (**NOTE**: I think this is only possible when you are using lists to represent the stacks unless you track the size of main and holder separately)
* Alternative Approach: I saw a number of different approaches which had the same time complexity but less actual runtime as a function of maybe:
  * Using lists and the `pop()` method (**NOTE**: Check the comprehensive Python cheatsheet or GeeksForGeeks)
  * Operating outside of the two stack limitation (e.g. only using one list)

### #225 Implement stack using queues
⌛00:00:00 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/implement-stack-using-queues/)

* Initial Approach: Content → **O(n)**, **O(1)**
* Solution Approach: Content → **O(n)**, **O(1)**
* Alternative Approach: Content → **O(n)**, **O(n)**

### #155 Min stack
⌛00:00:00 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/min-stack/)

* Initial Approach: Content → **O(n)**, **O(1)**
* Solution Approach: Content → **O(n)**, **O(1)**
* Alternative Approach: Content → **O(n)**, **O(n)**

### #1441 Build an array with stack operations
⌛00:00:00 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/build-an-array-with-stack-operations/)

* Initial Approach: Content → **O(n)**, **O(1)**
* Solution Approach: Content → **O(n)**, **O(1)**
* Alternative Approach: Content → **O(n)**, **O(n)**

### #633 Design Circular Queue
⌛00:00:00 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/design-circular-queue/)

* Initial Approach: Content → **O(n)**, **O(1)**
* Solution Approach: Content → **O(n)**, **O(1)**
* Alternative Approach: Content → **O(n)**, **O(n)**

### #1670 Design Front Middle Back Queue
⌛00:00:00 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/design-front-middle-back-queue/)

* Initial Approach: Content → **O(n)**, **O(1)**
* Solution Approach: Content → **O(n)**, **O(1)**
* Alternative Approach: Content → **O(n)**, **O(n)**

### #203 Removed linked list elements
⌛00:00:00 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/remove-linked-list-elements/)

* Initial Approach: Content → **O(n)**, **O(1)**
* Solution Approach: Content → **O(n)**, **O(1)**
* Alternative Approach: Content → **O(n)**, **O(n)**

### #203 Removed linked list elements
⌛00:00:00 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/remove-linked-list-elements/)

* Initial Approach: Content → **O(n)**, **O(1)**
* Solution Approach: Content → **O(n)**, **O(1)**
* Alternative Approach: Content → **O(n)**, **O(n)**


## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/