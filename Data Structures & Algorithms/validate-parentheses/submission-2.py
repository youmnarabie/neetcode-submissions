class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False 
        compliments = {"}": "{", "]": "[", ")": "("}
        stack = [] 
        for char in s: 
            # open 
            if char not in compliments.keys():
                stack.append(char)
            # close  
            else:
                if len(stack) == 0:
                    return False
                val = stack.pop()
                if val != compliments[char]:
                    return False
        return len(stack) == 0

        