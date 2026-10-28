class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # build up first subarray -- k long 
        # add it to answer if average meets criteria 
        subarr = arr[:k]
        ans = 0
        curr_sum = sum(subarr) 
        if curr_sum / k >= threshold:
            ans += 1 
        left = 0

        for i in range(k, len(arr)):
            curr_sum -= arr[left]
            left += 1 
            curr_sum += arr[i]
            if curr_sum / k >= threshold:
                ans += 1 
        return ans


        # until we reach the end: 
        # add a number and remove a number and recompute the average
        # update answer

        # return answer 