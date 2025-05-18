class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Sorting the given list of nums.
        res = [] # Creating a empty list.
        if len(nums)<3: #Check if length of the list is lesser than 3.
            return [] # Then return the empty list as output.
    # Here, We are using the two pointer method.
        for i in range(0,len(nums)-2): # Creating a loop to iterate through the list.
            l = i + 1 # Assigning the left pointer to i + 1.
            r = len(nums) - 1 # Assigning the right pointer to len(nums)-1 which starts from the another end of the list.
            if i>0 and nums[i] == nums[i-1]: # Checking if i-th current and pervious element is same means,
                continue # Continueing the loop, Just simply moves to the next element as i.
            while l < r: # Cheking if the left pointer is lesser then the right pointer.
                s = nums[i] + nums[l] + nums[r] # Then adding those three elements.
                if s == 0: # If the added elements are equals to 0 means,
                    res.append([nums[i],nums[l],nums[r]]) # Appending the values as a list to the res.
                    l += 1 # Incrementing the left pointer to 1.
                    r -= 1 # Decrementing the right pointer to -1, Because the right pointer is at the another end.
                    while l<r and nums[l]==nums[l-1]: # Loop used to detect the same values of left pointer, If yes means it increments the left pointer by 1.
                        l += 1 
                    while l<r and nums[r]==nums[r+1]: # Loop used to detect the same values of right pointer, If yes means it increments the left pointer by - 1.
                        r -= 1
                elif  s < 0: # If the s is lesser then 0 means we are incrementing the left pointer.
                    l += 1
                elif s > 0: # If the s is greater then 0 means we are incrementing the left pointer.
                    r -= 1
        return res # Return the result.
            