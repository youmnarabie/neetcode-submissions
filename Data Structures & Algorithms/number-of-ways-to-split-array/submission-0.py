class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            prefix.append(prefix[-1] + nums[i])
        
        count = 0 
        last = prefix[-1]
        for i in range(n - 1):
            remaining = last - prefix[i + 1] + nums[i + 1]
            if prefix[i] >= remaining:
                count += 1 

        return count
