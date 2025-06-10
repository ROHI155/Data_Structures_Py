from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list) # Opening a empty dictoinary with default keys for empty words.
        for i in strs: # loop to iterate through each element in the list.
            sort = ''.join(sorted(i)) # Assign the sort as the values of i in sorted way and group them as a single element.
            anagrams[sort].append(i) # append the  word i and the associated word sort as key to the dictionary.
        return list(anagrams.values()) # Return the list values of the anagrams.