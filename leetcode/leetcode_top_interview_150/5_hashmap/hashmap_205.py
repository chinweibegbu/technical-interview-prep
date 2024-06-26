def isIsomorphic_initial(s: str, t: str) -> bool:
    # Get all characters and their indices from both inputs
    sd = {}
    td = {}
    for i in range(len(s)):
        if (s[i] in sd):
            sd[s[i]].append(i)
        else:
            sd[s[i]] = [i]
    for j in range(len(t)):
        if (t[j] in td):
            td[t[j]].append(j)
        else:
            td[t[j]] = [j]

    # For each index list in t...
    for tt in td.values():
        #... If it is not in s' index lists, return False
        if (not (tt in list(sd.values()))):
            return False

    # If every index list is accounted for, return True
    return True

def isIsomorphic_solution(s: str, t: str) -> bool: 
    # Get all characters and their indices from both inputs
    sd = {}
    td = {}
    for i, s_char in enumerate(s):
        if (not (s_char in sd)):
            sd[s_char] = []
        sd[s_char].append(i)
    for j, t_char in enumerate(t):
        if (not (t_char in td)):
            td[t_char] = []
        td[t_char].append(j)
        
    # For each index list in t...
    for tt in td.values():
        #... If it is not in s' index lists, return False
        if (not (tt in list(sd.values()))):
            return False

    # If every index list is accounted for, return True
    return True