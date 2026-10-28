class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            counterpart = target - num
            if counterpart in seen:
                return [seen[counterpart], i] 
            seen[num] = i
        return []