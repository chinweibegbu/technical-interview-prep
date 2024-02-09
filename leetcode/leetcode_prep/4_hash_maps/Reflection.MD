# Solution Reflections
**Reflection Guide**:
* "*Initial Approach*" covers my initial approach(es)
* "*Solution Approach*" covers the approach I used that was accepted by all Leetcode testcases
* "*Optimal Approach*" covers an approach I saw in the submissions which I deemed to be more intuitive or easier than mine
* A single asterisk (*) by a point is used to indicate that an analysis as based on a Google search
* A double question mark (??) by a point is used to indicate a lack of trust in my personal analysis

## Hash Map Problems

### #705 Design hash set
⌛08:35:97 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/design-hashset/)

* Initial Approach: Use a list and its inbuilt functions (**NOTE**: Remember that a set must have only unique elements)
  * `add(key)`: Use `append(key)`. Only add key if it is not already in the set (logic error). → **O(1)**, **O(1)**
  * `contains(key)`: Use `in` operator → **O(n)**, **O(1)**
  * `remove(key)`: Use `remove(key)`. Only remove the key if it is in the set (runtime error). → **O(n)**, **O(1)**

⌛19:08:57 &nbsp;&nbsp; | CONSTRAINT: Use separate chaining

* Solution Approach #1: The set now has a fixed length, determined by a fixed size. Each slot in the array/list holds a linked list of all keys hashed to that location.
  * `add(key)`: Check that the key is NOT in the set. Get the index for chaining. If there is nothing there, create a LinkedListNode; else, add the key to the end of the existing chain. → **O(1)**, **O(1)**
  * `contains(key)`: Get the POTENTIAL index the key was chained to. Iterate through the linked list until key is found (return True) or you reach the end (return False) → **O(1)**, **O(1)**
  * `remove(key)`: Check that the key is in the set. Get the index it was chained to. If it is the head, point the slot to the head's next; else, keep track of prev and cur, iterate until cur has a val of key, then connect `prev.next` to `cur.next`. → **O(n)**, **O(1)**

**NOTE**: As expected this improved the actual relative runtime performance. I moved from ~700ms to ~150ms. The next thing I wonder is if I can reduce the number of times the linked list is iterated through (re: me checking to see if it is contained in the set before starting the actual operation).

⌛??:??:?? &nbsp;&nbsp; | CONSTRAINT: Use separate chaining + Reduce number of linked list parses

* Solution Approach #2:
  * `add(key)`: Get the index for chaining. If there is nothing there, create a LinkedListNode; else, parse through linked list until you reach the end (add the key) or you find the key there already (return). → **O(1)**, **O(1)**
  * `contains(key)`: Get the POTENTIAL index the key was chained to. Iterate through the linked list until key is found (return True) or you reach the end (return False) → **O(1)**, **O(1)**
  * `remove(key)`: Get the index it was chained to. If there is no linked list in the slot, return. If it is the head, point the slot to the head's next; else, keep track of prev and cur, iterate until cur has a val of key, then connect `prev.next` to `cur.next`. → **O(n)**, **O(1)**

### #706 Design hash map
⌛39:04:12 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/design-hashmap/)

* Solution Approach: Same as with #705 Solution Approach #2 but the LinkedListNode holds a pair (which is a list) rather than a val.
  * `put(key, value)`:
    * Get index and slot.
    * If there is a linked list in the spot, track prev and cur, then iterate through the linked list until you reach the end or find the key
      * If you find the key, update the pair
      * If you reach the end, add a new LinkedListNode with the pair
      <br> → **O(1)**, **O(1)**
  * `get(key)`:
    * Get index and slot
    * Iterate through the linked list until you find the key (return the value from the pair) OR you reach the end (return -1)
    <br> → **O(1)**, **O(1)**
  * `remove(key)`:
    * Get index and slot
    * If there is a linked list, continue
      * If the head is to be removed, point the slot to its `next`
      * Else, track prev and cur, and iterate. Then, if you reach the pair with the key, connect `prev.next` to `cur.next` 
    <br> → **O(1)**, **O(1)**
* Optimal Approach: Use a Python dictionary
  * `put(key, value)`: Use key-value assignment (handles both creating and updating) → **O(1)**, **O(1)**
  * `get(key)`: Check that key in `keys()`. If so, return its value. → **O(n)**, **O(1)**
  * `remove(key)`: Check that key in `keys()`. If so, use the `pop() method to delete it. → **O(1)**, **O(1)**

**THOUGHTS**: People were straight up using the Python dictionary which is so crazy to me because I thought that counted as an in-built hashmap... Read [this article] (https://programsquared.com/python/difference-between-dictionary-and-hashmap-in-python/). I guess that is the optimal approach but it seems too easy. I shall still implement it (don't be lazy, Chinwe).

**NOTE**: Another case of me not paying attention and just wanting to get the question over with. I had the approach down but I was making silly mistakes. A walkthrough would have also noted the bugs.

### #2283 Check if number is equal to digit count and digit value
⌛26:54:71 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/)

* Solution Approach:
  1. Store the length of the string in a variable n
  2. Parse the string to get the number of occurences of each digit
  3.  For each index and its value in string:
      * If the index is a key in occurences but it does not match the value, return False
      * If the index is NOT a key in occurences and it has a value of more than 0, return False
  1. If get out of the for loop, return True
  <br>→ **O(n)**, **O(1)**
  <br> **NOTE**: I reduced the actual time and space consumption by combining the different if statements resulting in the same thing into one statement and not storing the length in a variable before I used it.
* Optimal Approach:
  1. Use `Counter` from the `collections` library to create the occurences dictionary
  2. Use the `enumerate()` function to get the current index and value of the string in a neat an in-built fashion
  3. Use the dictionary `get(key, default)` function to get the value of the key and return a default value if it is not in the dictionary (**NOTE**: This will greatly simplify the if statement on line 56 in my solution code)
  <br>→ **O(n)**, **O(1)**
* Alternative Approach: Rather than first getting the occurences, check the number of occurences everytime you get to a new index with `str.count(el)` → **O(n<sup>2</sup>)**, **O(1)**
  
### #2261 K divisible element subarrays
⌛01:26:46:67 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/k-divisible-elements-subarrays/)

* Initial Approach: Initialise an empty list. Generate all subarrays. If subarray is valid and NOT in the list, add it. Return the length of the list. → **O(2<sup>n</sup>)**, **O(??)**
  <br>
  
  **NOTE**: This actually does not count as an initial approach as it did not pass all test cases. However, I added it here because the test cases were not all passed because I had exceeded the time limit (the algorithm itself was alright).

* Solution Approach: Same as initial approach:
  * Use a dictionary instead of a list so that you can separate the arrays by their length to reduce the number of comparisons when checking if it is NOT in the dictionary
  * Keep a counter every time you add a valid subarray so that you can directly return that rather than calculating the length of the dictionary by iterating through its keys and values
  → **O(2<sup>n</sup>)**, **O(??)**

  **THOUGHTS**: My relative performance is veeeery poor (faster than only 11% of submissions). I am yet to see what the girlies were doing to get such low runtimes. Maybe there was a way to do it without the O(2<sup>n</sup>) runtime???

* Optimal Approach:
  * Using a set. → **O(n)**, **O(1)**
    **THOUGHTS**: This is so embarrassing. Distinct elements and you didn't think of a set? Chai. Granted, I put this question in the "hash map" section and, the more I think about it, the more I realise the box that put me in while I was solving. → Actually, this did NOT work because set elements have to be hashable. → You do NOT have to store the arrays as arrays; you can make them strings or tuples.

**NOTE**: Hashable data types in Python are `int`, `float`, `str`, `tuple`, and `NoneType` 

### #633 Repeated DNA sequences
⌛13:06:34 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/repeated-dna-sequences/)

* Initial Approach: Sliding window + dictionary to store occurences. Iterate through dictionary `items()` to get sequences that occur more than once. → **O(n)**, **O(n)**
* Solution Approach: Same as initial approach but get sequences that occur more than once by using list comprehension on the dictionary's `items()` → **O(n)**, **O(n)**
* Optimal Approach: Same as Solution Approaoch with the following changes
  1. Change use of `range()` and `break` to `range(length-breakCondition)` → Removes an `if` statement
  2. If the sequence is in the dictionary, add it to the set that will be returned; Else, add it to the dictionary → Does not create the collection of valid sequences in a separate loop
  <br>→ **O(n)**, **O(n)**
* Alternative Approach: Same as Optimal Approach but use two sets → **O(n)**, **O(n)**

## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/