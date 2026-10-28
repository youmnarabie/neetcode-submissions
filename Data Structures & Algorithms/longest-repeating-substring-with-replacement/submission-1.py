from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = ans = maxf =  0
        counts = defaultdict(int)
        for right, char in enumerate(s): 
            counts[char] += 1 
            maxf = max(maxf, counts[char])

            while (right - left + 1) - maxf > k:
                counts[s[left]] -= 1 
                left += 1 

            ans = max(ans, right - left + 1)
        return ans