from typing import List

def sortArrayByParity(self, nums: List[int]) -> List[int]:
    solution = [0]*len(nums)
    even, odd = 0, len(nums)-1
    for num in nums:
        if (num%2==0):
            solution[even] = num
            even += 1
        else:
            solution[odd] = num
            odd -= 1
    return solution 