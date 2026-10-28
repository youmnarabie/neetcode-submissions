class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for num in nums[1:]:
            prefix.append(num + prefix[-1])

        left = prefix[0] 
        first = nums[0]
        right = prefix[len(nums) - 1]
        for i in range(len(nums)):
            right_sum = 0
            left_sum = 0
            if i != len(nums) - 1:
                right_sum = right - prefix[i + 1] + nums[i + 1]
            if i > 0:
                left_sum = prefix[i - 1] - left + first
            if right_sum == left_sum:
                return i
        return -1