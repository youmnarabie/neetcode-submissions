class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        right1 = m - 1 
        right2 = n - 1
        curr = len(nums1) - 1 

        while curr >= 0 and right1 >= 0 and right2 >= 0:
            val1 = nums1[right1]
            val2 = nums2[right2]
            if val1 >= val2:
                nums1[curr] = val1
                right1 -= 1  
            else:
                nums1[curr] = val2
                right2 -= 1 
            curr -= 1 
        while right1 >= 0:
            nums1[curr] = nums1[right1]
            right1 -= 1 
            curr -= 1
        while right2 >= 0:
            nums1[curr] = nums2[right2]
            right2 -= 1 
            curr -= 1 
        return nums1
            

