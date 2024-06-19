from typing import List

def threeSum_initial_FAILED(nums: List[int]) -> List[List[int]]:
    res = []
    present = {}
    nums.sort()
    for i in range(len(nums)):
        rem = nums[:i] + nums[i+1:]
        l, r = 0, len(rem)-1
        while l < r:
            if ((rem[l] + rem[r]) == (nums[i] * -1)):
                trio = [nums[i], rem[l], rem[r]]
                trio.sort()
                trio_str = "".join([str(i) for i in trio])
                if not(trio_str in present):
                    res.append(trio)
                    present[trio_str] = 1
                l += 1
            elif ((rem[l] + rem[r]) < (nums[i] * -1)):
                l += 1
            else:
                r -= 1
        
    return res

