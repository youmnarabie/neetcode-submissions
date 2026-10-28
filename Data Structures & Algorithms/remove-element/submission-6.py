class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0 

        for i, read in enumerate(nums):
            if read != val:
                nums[write] = read
                write += 1 
        return write


        
        