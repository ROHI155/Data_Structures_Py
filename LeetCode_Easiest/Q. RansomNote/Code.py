from typing import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        st1 = Counter(ransomNote) # Used to count the ransomNote strings.
        st2 = Counter(magazine) # Used to count the magazine strings.
        if st1 & st2 == st1: # Check if the str 1 and str2 equals to str1 then return True.
            return True 
        return False # Else return False.