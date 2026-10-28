class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        rightmost = len(nums) - 1
        while nums[rightmost] == val and rightmost >= 0:
            rightmost -= 1
        if rightmost < 0:
            return 0
        i = 0
        while i <= rightmost: 
            if nums[i] == val:
                nums[i], nums[rightmost] = nums[rightmost], nums[i]
                rightmost -= 1
            else:
                i += 1
        return rightmost + 1
