class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [0]*(2*n)
        for i, elem in enumerate(nums):
            ret[i] = ret[i+n] = elem
        return ret