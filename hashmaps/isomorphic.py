class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s_hash = {}
        t_hash = {}

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            if s_hash.get(s_char,-1) != t_hash.get(t_char,-1):
                return False
            s_hash[s_char] = i
            t_hash[t_char] = i
        return True
