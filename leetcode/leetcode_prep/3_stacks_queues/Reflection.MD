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
⌛21:41:92 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/implement-stack-using-queues/)

* Solution Approach: Keep track of two queues, main and holder, and the current size of the stack. Use `deque` from the `collections` library. Use `appendleft()` to insert to the back of the deque and `pop()` to remove from the front of the deque. 
  * `push()`: Add element to back of queue. Increment size. → **O(1)**, **O(1)**
  * `pop()`: Move all elements to holder. Reduce size by one. Move all but one element back to main. Return the last element in holder. → **O(n)**, **O(1)**
  * `top()`: Move all elements to holder, while keeping track of the last element popped. Move all elements back to main. Return the tracked last popped element. → **O(n)**, **O(1)**
  * `empty()`: Return whether size is greater than zero or not. → **O(1)**, **O(1)**
* Alternative Approach: Content → **O(n)**, **O(n)**

⌛07:00:88 &nbsp;&nbsp; | &nbsp;&nbsp; CONSTRAINT: Use only one queue

* Solution Approach: Keep track of a queue of type `deque` and the current size of the stack. 
  * `push()`: Add element to back of queue. Increment size. → **O(1)**, **O(1)**
  * `pop()`: Remove and add all but one element back to the queue. Reduce size by one. Return the new first element in the queue which was the LAST IN. → **O(n)**, **O(1)**
  * `top()`: Remove , note and add all elements back to the queue. Return the last noted element which was the LAST IN. → **O(n)**, **O(1)**
  * `empty()`: Return whether size is greater than zero or not. → **O(1)**, **O(1)**
* Optimal Approach: Same as mine above but utilise the `len()` function to figure out the number of elements in the queue. This removes the need to track size or initialise counter for looping.

**NOTE:** Remember to check what the constraints of the function are. Discuss this with the interviewer so that you code no less or more than is needed.
**NOTE**: Make a conscious effort to ensure your while loop has a stop condition and/or `break` statement

### #155 Min stack
⌛19:42:10 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/min-stack/)

* Solution Approach: Store elements in tuples, in the format (val, min), where min is the minimum value of the stack as at when it was entered. This works because we can only access elements in a specific order. 
  * `push()`: If stack is empty, add the element as (val, val). Else, get the minimum. If the new value is not less than the minimum, add the tuple as (val, minimum); else, add the tuple as (val, val) → **O(1)**, **O(1)**
  * `pop()`: Return the value of the top element tuple → **O(1)**, **O(1)**
  * `top()`: Remove and note the top element. Add it back to the stack. Return the value of the noted element tuple. → **O(1)**, **O(1)**
  * `getMin()`: Remove and note the top element. Add it back to the stack. Return the min of the noted element tuple. → **O(1)**, **O(1)** → **O(n)**, **O(1)**
* Alternative Approach:
  * Use a dictionary
  * Use a linked list
  * Use two stacks, main and minStack such that: (see solution explanation [here](https://leetcode.com/problems/min-stack/solutions/4182878/o-1-python-step-by-step-explanation)):
    * `push()`: Push new val to the stack. Get the top element and compare it to the new val, then add the minimum of those two to the minStack.
    * `pop()`: Pop from both stacks but only return the value from the main stack
    * `top()`: Return the value at the top of the main stack
    * `getMin()`: Return the value at the top of minStack <br>
  **NOTE**: This alternative is the same as my approach but it separates the tuples I am storing into two different stacks. 

### #1441 Build an array with stack operations
⌛20:26:86 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/build-an-array-with-stack-operations/)

* Solution Approach:
  1. Create an empty stack (with `deque`), a empty list (to hold operations) and index initialised to 0 to point to the current "target" element in the target array
  2. For x in range 1 to n+1 (which is the range for the stream we are provided):
      * Add x to the stack
      * Add "Push" to the operations list
      * If x does not match the current target, remove it and add "Pop" to the operations list
        * Else, increment the current target index by 1 (so that it is now pointing to the next element in target which we would NOT pop from the stack being constructed)
      * If the target array has been constructed (which can only happen when the stack and target array are the same length), break out of the loop
  3. Return the operations list
  → **O(n)**, **O(n)**

### #633 Design Circular Queue
⌛01:19:14:45 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/design-circular-queue/)

* Solution Approach: Used an array of a fixed size to implement the queue while keeping track of the index of the front element, rear element (**NOTE**: This is NOT the same as the element at the last index) and the size of the queue. 
  * `enQueue()`: → **O(n)**, **O(1)**
    * If full, return False
    * Iterate from the from to the first empty slot. Place new element in empty slot, update rear pointer and return True
  * `deQueue()`: → **O(1)**, **O(1)**
    * If empty, return False
    * Empty slot at front pointer
    * If there is anything else in the queue, update front pointer
    * Return True
  * `Front()`: If empty, return -1. Else, return element at front pointer. → **O(1)**, **O(1)**
  * `Rear()`: If empty, return -1. Else, return element at rear pointer. → **O(1)**, **O(1)**
  * `isEmpty()`: Return if both front pointer and last slot (NOT rear pointer) are both None. → **O(1)**, **O(1)**
  * `isFull()`: Return if both front pointer and last slot (NOT rear pointer) are both not None. → **O(1)**, **O(1)**

**THOUGHTS**: My runtime did sooooooooooo bad comparatively (only 9.2% faster than all users - insanely low, as I usually get between 60% and 80% faster). And, just by looking at one of the solutions, I realised what the issue was - I used a loop when they were really not needed at all in this code. So, I end up having an O(n) operation where it could be O(1) which is a humongous difference in efficiency. Implementing this increased my relative efficiency to 47.66% faster than all users. Also, I find it difficult to understand really streamlined code which is probably not good; I tend to go for more verbose but more easily understandable code.

**NOTE**: Be sure that your code is able to distinguish between 0 and `None`. Be as specific as possible e.g. `if (x is not None)` rather than `if (x)`. The former would fail for `None` only while the latter will fail for both `None` and 0, which are both falsy values. 

### #1670 Design Front Middle Back Queue
⌛38:00:00 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/design-front-middle-back-queue/)

* Initial Approach: Use a list and an element count updated with every push and/or pop operation. Add and split lists with the `+` and `[:]` operators. → **O(1)**, **O(n)** *
* Solution Approach: Use a list and an element count updated with every push and/or pop operation. Use in-built functions:
  * `insert(index, el)`
  * `append()`
  * `pop(index)`
  <br> → **O(1)**, **O(n)** *
* Optimal Approach: Same as mine but calculates the middle in a much more streamlined manner (see [here](https://leetcode.com/problems/design-front-middle-back-queue/solutions/3150143/python3-beats-100)).
* Alternative Approach: Using two deques (**NOTE**: I did not understand the code I saw with this approach. See one [here](https://leetcode.com/problems/design-front-middle-back-queue/solutions/4290658/o-1-with-simple-two-deques) and another [here](https://leetcode.com/problems/design-front-middle-back-queue/solutions/2912899/python-two-deques-easy-to-understand-o-1))

**THOUGHTS**: I had my approach pat down within the first five minutes but had trouble with finding the middle index. I think I was just not paying attention. I also did not do a walkthrough on paper before I started coding. If I paid more attention, this would not have happened.

**NOTE**: Go over in-built functions before an interview. Do not fix a broken wheel. If anything, just explain that you know the time and space efficiency of said wheel (hehe).

## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/