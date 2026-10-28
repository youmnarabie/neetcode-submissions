class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        ans = 0 

        for elem in nums:
            if elem == 1:
                curr += 1 
            else:
                ans = max(ans, curr)
                curr = 0
        return max(ans, curr)