# Solution Reflections
**Reflection Guide**:
* "*Initial Approach*" covers my initial approach(es)
* "*Solution Approach*" covers the approach I used that was accepted by all Leetcode testcases
* "*Optimal Approach*" covers an approach I saw in the submissions which I deemed to be more intuitive or easier than mine
* A single asterisk (*) by a point is used to indicate that an analysis as based on a Google search
* A double question mark (??) by a point is used to indicate a lack of trust in my personal analysis

## Sorting Algorithm Problems

### #201 Valid Anagram
⌛05:27:67 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/valid-anagram/)

* Initial Approach: If strings are not the same length, return False. Use dictionaries to count character occurences and compare them. → **O(n)**, **O(n)**
* Solution Approach: Use Python's in-built `sorted()` function to compare them. → **O(n logn)**, **O(n)*** 
  <br>**NOTE**: "*The primary difference between the list sort() function and the `sorted()` function is that the `sort()` function will modify the list it is called on. The `sorted()` function will create a new list containing a sorted version of the list it is give*" (Source: [codecademy-forum-post](https://discuss.codecademy.com/t/what-is-the-difference-between-sort-and-sorted/349679#:~:text=The%20primary%20difference%20between%20the,the%20list%20it%20is%20given.))
* Optimal Approach: Solution approach + checking that they are the same length before comparison → **O(n logn)**, **O(n)*** 
* Alternative Approaches:
  * Initial approach BUT use arrays of length character set to store the character counts and compare those rather than dictionaries → **O(n)**, **O(1)** 
  * Initial approach BUT use the `Counter` class from the `collections` library → **O(n)**, **O(n)*** 
  <br>**NOTE**: If you can import libraries, always use the counter over the dictionary. It does the same thing and shows your knowledge of the language.

### #169 Majority Element
⌛05:28:54 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/majority-element/)

* Initial Approach: Sort list with `sort()` so that it is in-place. Return the value right after the halfway point i.e. at index len(nums)//2. → **O(n logn)**, **O(1)**
  
* Solution Approach: Use a dictionary to count occurences. If the count of the current element every becomes more then len(nums)//2, return said elememt → **O(n)**, **O(n)**
  
* Optimal Approach: Boyer-Moore sorting algorithm → **O(n)**, **O(1)**
  * [Link to solution](https://leetcode.com/problems/majority-element/solutions/4713145/hashtable-boyer-moore-majority-vote-algo-bit-manip-las-vegas-3ms-beats-99-85) which instroduced me to the algorithm
  * [Link to explanation article](https://www.geeksforgeeks.org/boyer-moore-majority-voting-algorithm/) by GeeksForGeeks
* Alternative Approach: → **O(n)**, **O(n)** 
  1. Create a set of all unique elements in the list using `set()`
  2. For each element in the set, if its `count()` is more than len(nums)//2, return it

**NOTE**: Is there any way that I could have come up with an O(n) time complexity, O(1) space complexity algorithm? I don't know and that bothers me.

### #506 Relative Ranks
⌛15:10:24 &nbsp;&nbsp; | &nbsp;&nbsp; See problem [here](https://leetcode.com/problems/relative-ranks/)

* Initial Approach: → **O(n<sup>2</sup>)**, **O(n)**
  1. Store a sorted and reversed version of the score array in a new variable
  2. Create a variable to store the length of score
  3. Create an array of length n to return
  4. At each index in range n:
     1. Get the current score in the unsorted score array
     2. Get the position/index of said score in the sorted array using the `index()` function
      <br>**NOTE**: I noticed this only after looking after seeing the optimal solution but this is an O(n) operation, meaning that the entire loop that is step 4 becomes an O(n<sup>2</sup>) operation
     3. Determine the place based on the position/index in the sorted array >>> Use an dictionary to hold the first to third place resulting strings
     4. Insert the determined place at the current index in the answer array
  5. Return the answer array
* Solution Approach: Same as Intial approach but with the following improvements: → **O(n<sup>2</sup>)**, **O(n)**
  * Replace the dictionary with an array
  * Store the place results in the score array rather than creating a new array
  * Forget reversal and just calculate the position by subtracting its sorted array index from its length
  <br> → **O(n logn)**, **O(n)**
* Optimal Approach: → **O(n logn)**, **O(n)**
  1. Use dictionary comprehension to create a map of scores to their original index in the unsorted score array → *O(n), O(n)*
   
  2. Create a array of length n to return to hold the places → *O(n), O(n)*
   
  3. For i in range n: → *O(n), O(1)*
     1. Get the current element in the sorted array
     2. Get the original index of the element in the unsorted array
     3. Assign place to original index in answer array
   
  4. Return the answer array → *O(1), O(1)*
   
**THOUGHTS**: In my opinion, this approach has the same idea as my initial approach but takes a different route. It notes the indices first and then places them, rather than... Oh, I see the difference. It only parses the array once such that step 4-2 in my initial approach which is O(n) ON EACH ITERATION, does not... wow, now that I think about it, my initial approach was actually O(n<sup>2</sup>)... woooooooow, I did NOT realise that. 

**NOTE**: When doing a walkthrough of yoru problem, include an intentional runtime (and space) complexity analysis for EACH LINE and then for the entire function based on the analysis of each line. >>> It not being in a loop or being in a single line does NOT mean it has a runtime complexity of O(1). 

## Markdown Resources
GitHub Emojis: https://github-emoji-picker.rickstaa.dev/