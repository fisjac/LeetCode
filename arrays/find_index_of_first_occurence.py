class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # initialize start
        # loop through haystack (i)
        # if haystack[i] == needle[j]: j++
        # if j == len(needle): return start
        i = 0
        remove = []
        matches = {}

        while i < len(haystack):
            for start, j in matches.items():
                # print('checking', start)
                print(haystack[start:i+1], needle[j])
                if haystack[i] == needle[j]:
                    j += 1
                    if j == len(needle):
                        return start
                    matches[start] = j
                else:
                    remove.append(start)

            while len(remove) > 0:
                start = remove.pop()
                # print('removing', start)
                del matches[start]

            if haystack[i] == needle[0]:
                # print('found new beginning at', i)
                if len(needle) == 1: return i
                matches[i] = 1

            i += 1
        return -1
