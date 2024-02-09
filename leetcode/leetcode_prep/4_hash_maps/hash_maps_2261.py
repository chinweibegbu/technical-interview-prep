from collections import List

def countDistinct_Initial(self, nums: List[int], k: int, p: int) -> int:
    counter = []
    for i in range(1, len(nums)+1):
        for j in range(len(nums)):
            # Generate subarray
            if (j+i > len(nums)):
                continue
            elif (j+i == len(nums)):
                arr = nums[j:]
            else:
                arr = nums[j:j+i]
            
            # print("i:{} start:{} end:{} arr:{}".format(i, j, j+i if (j+i < len(nums)) else "-", arr))

            # Check if it has at most k elements divisible by p
            valid = len([a for a in arr if (a%p == 0)]) <= k

            # Check that it is distinct
            if ((not(arr in counter)) and valid):
                counter.append(arr)
                # print("Added {}".format(arr))
            # else: print("Ignored {}".format(arr))

    return len(counter)
        
def countDistinct_Solution(self, nums: List[int], k: int, p: int) -> int:
    counter = {}
    distinct_count = 0
    for i in range(1, len(nums)+1):
        for j in range(len(nums)):
            # Generate subarray
            if (j+i > len(nums)):
                continue
            elif (j+i == len(nums)):
                arr = nums[j:]
            else:
                arr = nums[j:j+i]
            
            # print("i:{} start:{} end:{} arr:{}".format(i, j, j+i if (j+i < len(nums)) else "-", arr))

            # Check if it has at most k elements divisible by p
            valid = len([a for a in arr if (a%p == 0)]) <= k

            # Check that it is distinct
            if ((valid) and (not(arr in counter.get(len(arr), [])))):
                counter[len(arr)] = counter.get(len(arr), []) + [arr]
                distinct_count += 1
                # print("Added {}".format(arr))
            # else: print("Ignored {}".format(arr))

    return distinct_count

def countDistinct_Optimal_Tuple(self, nums: List[int], k: int, p: int) -> int:
        res = set()
        N = len(nums)

        for i in range(N):
            count = 0

            for j in range(i, N):
                if nums[j] % p == 0:
                    count += 1
                if count > k:
                    break
                
                res.add(tuple(nums[i:j + 1]))

        return len(res)
    
def countDistinct_Optimal_String(self, nums: List[int], k: int, p: int) -> int:
    my_set = set()
    for i in range(len(nums)):
        count = 0
        sb = ""
        for j in range(i, len(nums)):
            if nums[j] % p == 0:
                count += 1
            if count > k:
                break
            sb += str(nums[j]) + "_"
            my_set.add(sb)
    return len(my_set)
                