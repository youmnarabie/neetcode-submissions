class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a", "e", "i", "o", "u"])

        ans = 0 
        for i in range(k):
            if s[i] in vowels:
                ans += 1 
        left = 0
        curr = ans
        for index in range(k, len(s)):
            if s[left] in vowels:
                curr -= 1 
            if s[index] in vowels:
                curr += 1 

            ans = max(ans, curr)
            left += 1 

        return ans



