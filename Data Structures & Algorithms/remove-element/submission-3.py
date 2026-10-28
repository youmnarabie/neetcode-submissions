class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        rightmost = len(nums)
        i = 0
        while i < rightmost: 
            if nums[i] == val:
                nums[i] = nums[rightmost - 1]
                rightmost -= 1
            else:
                i += 1
        return rightmost
