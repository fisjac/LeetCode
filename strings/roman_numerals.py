class Solution:
    def romanToInt(self, s: str) -> int:
        translation = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0
        current_char_val = 0
        for i in range(len(s)-1,-1,-1):
            current_val = translation[s[i]]
            if current_val >= current_char_val:
                current_char_val = current_val
                res += current_val
            else:
                res -= current_val

        return res
