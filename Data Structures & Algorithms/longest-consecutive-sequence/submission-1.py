from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        available = set(nums)
        ans = curr = 0 
        if len(nums) == 0:
            return ans 

        val = nums[0]
        for num in available:
            if num - 1 not in available:
                curr = 1 
                val = num 

            while val + 1 in available:
                val += 1 
                curr += 1 
            
            ans = max(ans, curr)
            
        return ans 
        