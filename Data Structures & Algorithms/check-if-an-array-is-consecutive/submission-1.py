class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        return len(nums) == max(nums) - min(nums) + 1 and len(set(nums)) == len(nums)