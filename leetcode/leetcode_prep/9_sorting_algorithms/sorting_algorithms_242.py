class Solution_Initial:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False

        counter_s, counter_t = {}, {}
        for i in range(len(s)):
            counter_s[s[i]] = counter_s[s[i]]+1 if s[i] in counter_s else 1
            counter_t[t[i]] = counter_t[t[i]]+1 if t[i] in counter_t else 1 

        return counter_s == counter_t          

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)    

class Solution_Optimal:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return sorted(s) == sorted(t)    

class Solution_Alternative_1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        arr_s = [0]*26
        arr_t = [0]*26

        for value in s:
            index = ord(value) - ord('a')
            arr_s[index]+=1
        
        
        for value in t:
            index = ord(value) - ord('a')
            arr_t[index]+=1
        
        return arr_s == arr_t

from collections import Counter
class Solution_Optimal:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return Counter(s) == Counter(t)  