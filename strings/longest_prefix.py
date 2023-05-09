class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min([len(string) for string in strs])
        i = 0
        while i < min_length:
            char = strs[0][i]
            for string in strs:
                if string[i] != char:
                    if i == 0: return ''
                    else: return strs[0][0:i]
            i += 1

        return strs[0][0:i]
