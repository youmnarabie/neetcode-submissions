class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums.sort()
        smallest = nums[0]

        for i, num in enumerate(range(smallest, smallest+len(nums))):
            if num != nums[i]:
                return False
        return True
