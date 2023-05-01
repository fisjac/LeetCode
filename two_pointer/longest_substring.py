from collections import defaultdict
class Solution:
   def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = defaultdict(int)
        longest = 0
        max_f = 0

        for r in range(len(s)):

            count[s[r]] = count.get(s[r], 0) + 1
            max_f = max(max_f, count[s[r]])
            while (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)
        return longest

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if len(s) <= 1: return len(s)

    #     seen = set()
    #     l, r = 0,0
    #     longest = 0
    #     while r < len(s):
    #         while s[r] in seen:
    #             seen.remove(s[l])
    #             l += 1
    #         seen.add(s[r])
    #         r += 1
    #         longest = max(longest, r - l)

    #     return longest
