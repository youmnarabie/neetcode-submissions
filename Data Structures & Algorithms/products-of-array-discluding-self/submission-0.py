class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0 
        ret = [0] * len(nums)
        for num in nums:
            if num != 0:
                product *= num 
            else:
                zeros += 1 
        if zeros > 1:
            return ret
        
        for i, num in enumerate(nums):
            if zeros:
                if num == 0:
                    ret[i] = product
                else:
                    ret[i] = 0 
            else:
                ret[i] = product // num
        return ret