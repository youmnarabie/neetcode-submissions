from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        return Counter(nums).most_common()[0][1] > 1