class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = []
        for string in strs:
            ret.extend([str(len(string)), "#", string])
        return "".join(ret)

    def decode(self, s: str) -> List[str]:
        print("Decoding ", s)
        ret = []
        i = 0
        while i < len(s): 
            j = i
            while s[j] != "#":
                j += 1 
            length = int(s[i:j])
            ret.append(s[j + 1 : j + 1 +length])
            i = j + 1 + length
        return ret


