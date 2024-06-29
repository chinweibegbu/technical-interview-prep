# Solution Reflections
**Reflection Guide**:
* "*Initial Approach*" covers my initial approach(es)
* "*Solution Approach*" covers the approach I used that was accepted by all Leetcode testcases
* "*Optimal Approach*" covers an approach I saw in the submissions which I deemed to be more intuitive or easier than mine
* A single asterisk (*) by a point is used to indicate that an analysis as based on a Google search
* A double question mark (??) by a point is used to indicate a lack of trust in my personal analysis
* --:--:-- in the time slot means that I couldn't solve it on my own

## Intervals Problems

### #228 Summary Ranges
⌛09:03:76 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150)

* Solution Approach: → **O(n)**, **O(1)**
  * **IDEA**: Because the array is sorted and unique, we know that the current sequence has been broken when the next element is not the current element plus one and, so, we can summarise that particular sequence
  * **ALGORITHM**:
    1. Initialise result to an empty array
    2. Intialise left and right pointers, l and r, to the beginning of the array
    3. For each index and element in the array (using the `enumerate()` function):
       1. If we are at the end of the array or the sequence has been broken:
          1. If there is exactly one element in the current sequence, add just that element to result
          2. Else, add both the elements with the joining characters, "->" to result
          3.  update l and r to both point to the next element
      1.  Else, increment r
    4. Return result

**THOUGHTS**: I learned from the approach Neetcode used for the Longest Consecutive Sequence question (see reflection for question #128 in `../5_hashmap/Reflection.MD` and code in `longestConsecutive_optimal_2()` function in `../5_hashmap/hashmap_128.py`)

### #56 Merge Intervals
⌛25:38:56 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/merge-intervals/description/?envType=study-plan-v2&envId=top-interview-150)

* Solution Approach: → **O(n<sup>2</sup>)**, **O(n)**
  * **IDEA**: Sort intervals then iterate through intervals and compare their ends to determine what can be merged
  * **ALGORITHM**: See comments of `merge_solution()` function in `./intervals_56.py`

NOTE: You can pass a `key` named parameter to the in-place Python `list.sort()` function. It takes a function which returns how each element in the `list` should be sorted e.g.

![Python sort() key parameter usage](python_sort_key.png)

## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/