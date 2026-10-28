class Solution:
    def isValid(self, s: str) -> bool:
        close_open = {"}": "{", "]":"[", ")": "("}
        stack = []
        for char in s:
            if char in close_open.keys():
                # ensure the last seen one is its open 
                if not stack or stack.pop() != close_open[char]:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0
