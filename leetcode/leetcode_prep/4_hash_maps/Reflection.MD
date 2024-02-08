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
⌛19:42:10 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/)

* Solution Approach: Content → **O(n)**, **O(1)**
  
### #2261 K divisible element subarrays
⌛20:26:86 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/k-divisible-elements-subarrays/)

* Solution Approach: Content → **O(n)**, **O(1)**

### #633 Repeated DNA sequences
⌛01:19:14:45 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/repeated-dna-sequences/)

* Solution Approach: Content → **O(n)**, **O(1)**

## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/