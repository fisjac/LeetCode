class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def _backtrack(o,c, s):
            if len(s) == n * 2:
                ans.append(s)

            # open case
            if o < n:
                _backtrack(o + 1, c, s + '(')

            # close case
            if o > c:
                _backtrack(o, c + 1, s + ')')

        _backtrack(0, 0, '')
        return ans
