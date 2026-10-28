class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = float("-inf")
        rev = [0]*len(arr)
        rev[-1] = -1  
        for i in range(len(arr)-1, 0, -1):
            max_so_far = max(arr[i], max_so_far)
            rev[i-1] = max_so_far 
        return rev