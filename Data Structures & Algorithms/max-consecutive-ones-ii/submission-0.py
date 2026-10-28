class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # count number of zeroes
        # want longest subarray
        # subarray becomes invalid if we have > 1 zero 
        # narrow window until we have <= 1 zero again 

        left = curr = ans = 0 
        for right, num in enumerate(nums): 
            if num == 0:
                curr += 1 

            while curr > 1:
                if nums[left] == 0:
                    curr -= 1
                left += 1 

            ans = max(ans, right - left + 1)
        
        return ans