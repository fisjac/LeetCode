class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counts = {}
        for char in magazine:
            counts[char] = counts.get(char,0) + 1
        for char in ransomNote:
            counts[char] = counts.get(char,0) - 1
            if counts[char] < 0: return False
        return True
