class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0 

        left = ans = 0 
        curr = 1
        for right, num in enumerate(nums): 
            curr *= num 

            while curr >= k:
                curr //= nums[left]
                left += 1 
            
            ans += right - left + 1
        return ans