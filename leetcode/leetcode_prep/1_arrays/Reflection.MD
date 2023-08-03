# Solution Reflections
**Reflection Guide**:
* "*Solution Approach*" covers the approach I used that was accepted by all Leetcode testcases while "*Optimal Approach*" covers an approach I saw in the submissions which I deemed to be more intuitive or easier than mine
* A single asterisk (*) by a point is used to indicate that an analysis as based on a Google search
* A double question mark (??) by a point is used to indicate a lack of trust in my personal analysis

## Array Problems
### #26 Remove duplicates from sorted array 
⌛00:52:08 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/remove-duplicates-from-sorted-array)

* Initial Approach: If an element is the same as the element before it, bubble it up to the end of the array → **O(n<sup>2</sup>)**
* Solution Approach: Use pointers to swap elements if they are unique and return → **O(n)**

### #896 Monotonic array
⌛00:18:09 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/monotonic-array/)

* Initial Approach: Check if the pattern (decreasing or increasing) is continuing for each triad of elements → **O(n)**
* Solution Approach: Check pattern, THEN check if expected pattern is continuing for each triad of elements → **O(n)**
* Optimal Approach: Check if array is sorted using the in-built `sorted()` function → **O(n log n)** *

### #905 Sort array by parity
⌛00:06:54 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/sort-array-by-parity/)

* Solution Approach: Create array of the length of the original array. Place elements in the new array based on even or odd to either the beginning or end of new array. Update pointer to beginning and end based on what was entered → **O(n)** ??
* Optimal Approach: Use list comprehensions (more intuitive) → **O(n)** *
  
  **NOTE**: In my original brainstorming, list comprehensions came to mind. The reason I did not use them was because, in the moment, I was not sure what the complexity of list comprehension is. Right now, I think it would be **O(n)** because it will evaluate the condition for every element in a list of size n, but I am not sure.

### #88 Merge sorted lists
⌛00:52:27 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/merge-sorted-array/)

* Initial Approach: Try swapping elements and keeping swapped out elements in a stack → **O(?)**
* Solution Approach: Get the beginning of the first list. Merge arrays the way you would with merge sort → **O(n+m)**

  **NOTE**: See the `merge()` function in `[dsa_with_python\algorithms\sorting_algorithms\merge_sort.py]` for a more intuitive approach

* Optimal Approach: See the `merge_optimal()` function in `[dsa_with_python\leetcocde\leetcode_prep\1_arrays\array_88.py]` file to see the optimal approach's core (I genuinely do not know how to summarise the pseusocode - I'm still not sure about how it works) → **O(n+m)** *

### #942 Valid mountain array
⌛00:28:48 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/valid-mountain-array/)

* Solution Approach: Move from both ends until you reach a peak (i.e. when there is a swap). If the pointers are equal, they peaked at the same place and, thus, it is a valid mountain array → **O(n)**

  **NOTE**: Like, I had an approach and I got it to work but I don't understand the code that I wrote. 

THOUGHTS: I don't feel like I succeeded here. I would like to re-try it sometime. My time complexity was horrid. I actually tried a different approach but was unable to code what was in my head - that is something that I need to work on. If I cannot translate ideas to code... that's a problem. Additionally, I did not understand any of the solution code so I have no optimal solution (for now). Tough one to implement for me.


## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/