class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ret = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            left_val = nums[left]
            right_val = nums[right]
            if abs(left_val) > abs(right_val):
                ret[i] = left_val**2 
                left += 1
            else:
                ret[i] = right_val**2
                right -= 1 
        return ret