from collections import List

class Solution_1:
    def thirdMax(self, nums: List[int]) -> int:
        distict_nums = set(nums)
        
        if (len(distict_nums) < 3):
            return max(distict_nums)
        else:
            return sorted(distict_nums)[-3]

class Solution_2:
    def thirdMax(self, nums: List[int]) -> int:
        return sorted(set(nums))[-3] if (len(set(nums)) >= 3) else max(set(nums))