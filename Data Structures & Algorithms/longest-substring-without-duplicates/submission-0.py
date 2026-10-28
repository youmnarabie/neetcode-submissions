class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = ans = 0 
        window = set() 

        for right, char in enumerate(s): 
            while char in window: 
                window.remove(s[left])
                left += 1 
            window.add(char)

            ans = max(ans, right - left + 1)
        return ans