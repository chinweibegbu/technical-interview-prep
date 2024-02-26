from collections import List

class Solution_Initial:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for n in nums:
            counter[n] = counter[n]+1 if (n in counter) else 1
            if (counter[n] > len(nums)//2):
                return n
            
class Solution_Optimal:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        votes = 0
        
        for num in nums:
            # If the current candidate has no votes, i.e. it occured less than len(nums)//2 times, replace the candidate and reset its votes
            if (votes == 0):
                candidate = num
                votes = 1
            else:
                # WHY THE FOLLOWING? Because any element that is NOT the majority element will cause votes to return to 0 because it does not occur more than all the other elements
                if (num == candidate):
                    votes += 1
                else:
                    votes -= 1
        
        # We return the candidate without actually counting its occurence because the question said that we could assume that a majority element exists
        return candidate
                
class Solution_Alternative:
    def majorityElement(self, nums: List[int]) -> int:
        elements = set(nums)
        for e in elements:
            if (nums.count(e) > len(nums)//2):
                return e