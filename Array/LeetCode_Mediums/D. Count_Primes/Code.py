class Solution:
    def countPrimes(self, n: int) -> int:
        arr = [True]*n # Firstly marking all the elements as true.
        if n == 0 or n == 1: # Nextly Checking the 0 or 1 occurs means return as 0.
            return 0
        
        arr[0],arr[1] =False,False # Then assigning the element 0 and 1 as False
        for i in range (2,int(n**0.5)+1): # Entering to the loop through the range of starting from 2 to int(n**0.5)+1.
            if arr[i]: # Condition proceeds if the i has value in array
                for j in range(i+i,n,i): # Entering to the another loop of j for marking the multiples of i as False
                    arr[j] = False
        return sum(arr) # Return the array.