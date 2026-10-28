class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        left = curr = 0 
        for right, num in enumerate(nums):
            curr += num
            while curr >= target: 
                ans = min(ans, right - left + 1)

                curr -= nums[left]
                left += 1 
            
        if ans == float("inf"):
            return 0 
        return ans

