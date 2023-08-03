from typing import List

# !!!REVIST THIS FUNCTION 
def validMountainArray(self, arr: List[int]) -> bool:
    if len(arr) < 3:
        return False

    print(arr)
    i, j = 0, len(arr)-1
    reachedPeakLeft, reachedPeakRight = False, False
    for x in range(len(arr)):
        if ((arr[i] >= arr[i+1]) or (i+1 == len(arr)-1)):
            print("We've peaked LEFT | i={}".format(i))
            reachedPeakLeft = True
        else:
            i+=1
            print("Moved from LEFT | i={}".format(i))

        if ((arr[j] >= arr[j-1]) or (j-1 == 0)):
            print("We've peaked RIGHT | j={}".format(j))
            reachedPeakRight = True
        else:
            j-=1
            print("Moved from RIGHT | j={}".format(j))
    
    if (i==j):
        return True
    return False