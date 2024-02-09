def digitCount(self, num: str) -> bool:
    # Get string length:
    n = len(num)
    
    # Parse string to store digit occurences
    occurences = {}
    for s in num:
        s = int(s)
        if (s in occurences.keys()):
            occurences[s] += 1
        else:
            occurences[s] = 1

    # Compare indices to occurences
    for i, s in zip(range(n), num):
        s = int(s)
        if ((i in occurences.keys()) and (occurences[i] != s)):
            return False
        elif ((not (i in occurences.keys()) and (s > 0))):
            return False
    return True

def digitCount_Solution_1(self, num: str) -> bool:
    # Get string length:
    n = len(num)
    
    # Parse string to store digit occurences
    occurences = {}
    for s in num:
        s = int(s)
        if (s in occurences.keys()):
            occurences[s] += 1
        else:
            occurences[s] = 1

    # Compare indices to occurences
    for i, s in zip(range(n), num):
        s = int(s)
        if (((i in occurences.keys()) and (occurences[i] != s)) or ((not (i in occurences.keys()) and (s > 0)))):
            return False
    return True
        
def digitCount_Solution_2(self, num: str) -> bool:
    # Parse string to store digit occurences
    occurences = {}
    for s in num:
        s = int(s)
        if (s in occurences.keys()):
            occurences[s] += 1
        else:
            occurences[s] = 1

    # Compare indices to occurences
    for i, s in zip(range(len(num)), num):
        s = int(s)
        if (((i in occurences.keys()) and (occurences[i] != s)) or ((not (i in occurences.keys()) and (s > 0)))):
            return False
    return True

from collections import Counter
def digitCount_Optimal(self, num: str) -> bool:
    ctr = Counter(num)
    for i,v in enumerate(num): 
        if ctr.get(str(i), 0) != int(v): 
            return False
    return True
