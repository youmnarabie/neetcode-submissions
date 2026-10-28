class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = curr = 0 
        ans = float("inf")

        # for each RIGHT element in nums starting from the beginning
        # add the right element to the tracker
        # check if we meet the condition 
        # --> update the answer
        # --> continuously update left until the condition is no longer met OR the pointers meet
        # --> update the answer 

        for right, num in enumerate(nums):
            curr += num
            while curr >= target:
                ans = min(ans, right - left + 1)
                curr -= nums[left]
                left += 1 
        if ans == float("inf"):
            return 0
        return ans