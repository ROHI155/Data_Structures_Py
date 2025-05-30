class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = set(nums1),set(nums2) # Removing the Duplicates
        output = [] # Creating an empty List to store the output
        for i in nums1: # Looping through the first List
            if i in nums2: # Checking if the element is present in the second List
                output.append(i) # If present, append it to the output List
        return output # Returning the output List
        