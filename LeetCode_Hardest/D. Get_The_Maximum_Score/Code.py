class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        # Here assigning a and b as length of nums 1 and nums 2
        a = len(nums1)
        b = len(nums2)
        # Assigning i,j,sum1,sum2,res as 0.
        i = 0
        j = 0 
        sum1 = 0
        sum2 = 0
        res = 0
        # Entering into a while loop with the condition of i lesser than a and j lesser than b.
        while i<a and j<b:
            # Checking if the nums1[1] is lesser than nums2[j].
            if nums1[i]<nums2[j]:
                sum1+=nums1[i] # If true means perform sum1 + nums1[i] and increment the i to plus 1.
                i += 1
            # Checking the second condition if nums1[i] greater than the nums2[j]
            elif nums1[i]>nums2[j]:
                sum2+=nums2[j] # If true means perform sum2 = nums2[j] and increment j by 1.
                j += 1
            # Else perform the result operation on comparing the max element sum1 and sum2 and then add it with nums[i] and assign the sum1 and sum2 as 0.
            # Increment the i and j by 1. 
            else:
                res += nums1[i]+max(sum1,sum2)
                sum1 = 0
                sum2 = 0
                i += 1
                j += 1
        # Create the loop if the nums1 is only given 
        while i<a:
            sum1 += nums1[i]
            i += 1
        # Create the loop if the nums2 is only given
        while j<b:
            sum2 += nums2[j]
            j += 1
        # Perform results in case of either nums1 or nums2 is missing.
        res += max(sum1,sum2)
        # Return the result with the mod of value (10**9)+7
        return res%((10**9)+7)