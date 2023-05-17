class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_arr = s.split(' ')
        if len(word_arr) != len(pattern): return False

        char_hash = {}
        word_hash = {}
        for i in range(len(pattern)):
            char_pos = char_hash.get(pattern[i], -1)
            word_pos = word_hash.get(word_arr[i], -1)
            if char_pos != word_pos:
                return False
            char_hash[pattern[i]] = i
            word_hash[word_arr[i]] = i
        return True
