class Solution:
    def reverseWords(self, s: str) -> str:
        split_list = s.split(" ")
        ret = []
        for word in split_list:
            ret.append("".join(word[::-1]))
        return " ".join(ret)
