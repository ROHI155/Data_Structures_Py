class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums) # Here this will asigns the k with the modulo of the given len nums.
        nums[:] = nums[::-1] # Here it first reverses the given set of inputs. and splits into two parts.
        nums[k:] = nums[k:] [::-1] # Then it reverses the first set of elements. 
        nums[:k] = nums[:k] [::-1] # Then it reverses the last set of elements.
        return nums # return nums in the end 