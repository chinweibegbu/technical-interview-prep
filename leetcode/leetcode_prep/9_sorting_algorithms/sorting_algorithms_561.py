from collections import List

class Solution_1:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort array (in-place) >>  O(n logn), O(1)
        nums.sort()

        # For every pair, add the difference of the first and second to sum
        msp = 0
        for i in range(0, len(nums), 2):
            msp += min(nums[i], nums[i+1])

        # Return sum
        return msp
    
class Solution_2:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort array (in-place) >>  O(n logn), O(1)
        nums.sort()

        # For every pair, add the first element to the sum
        msp = 0
        for i in range(0, len(nums), 2):
            msp += nums[i]

        # Return sum
        return msp

class Solution_3:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort array (in-place) >>  O(n logn), O(1)
        nums.sort()

        # Return the sum of every other element (which is the min for each pair)
        return sum([nums[i] for i in range(0, len(nums), 2)])
    
class Solution_Optimal:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Same as my approaches but streamlined and using list indexing rather than list comprehension
        return sum(sorted(nums)[::2])