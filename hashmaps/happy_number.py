class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def _recurse(n):
            if n == 1: return True
            n_string = ''.join(sorted(str(n)))
            if n_string in seen: return False
            else:seen.add(n_string)
            total = sum([int(digit) ** 2 for digit in n_string])
            return _recurse(total)
        return _recurse(n)
