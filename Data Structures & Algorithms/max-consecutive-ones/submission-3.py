class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = curr = ans = 0

        for right, num in enumerate(nums):
            if num == 1:
                curr += 1 
                ans = max(ans, curr)
            else:
                curr = 0
        
        return ans

