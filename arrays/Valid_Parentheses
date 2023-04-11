class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        for char in s:
            if char in '([{':
                stack.append(lookup[char])
            elif char in ')}]':
                if len(stack) == 0: return False
                current = stack.pop()
                if current != char:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
