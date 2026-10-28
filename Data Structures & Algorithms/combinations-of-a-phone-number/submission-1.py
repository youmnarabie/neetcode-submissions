from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        maps = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        candidates = []
        for char in digits:
            candidates.append(list(maps[char]))
        ret = []
        for combo in product(*candidates):
            ret.append("".join(combo))
        return  ret
