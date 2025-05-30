class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low = 0
        high = nums[-1] - nums[0]      
        
        def count_pairs(max):
            count = 0
            j = 0
            for i in range(len(nums)):
                while(j < len(nums) and nums[j] - nums[i] <= max):
                    j += 1
                count += j - i - 1
            return count


        while (low < high):
            mid = (low + high) // 2
            if (count_pairs(mid) < k):
                low = mid + 1
            else: 
                high = mid
        return low