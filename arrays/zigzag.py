class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [''] * numRows
        down = True
        row = 0
        for char in s:
            rows[row] += char
            if numRows > 1:
                row += 1 if down else -1
            if row == numRows - 1: down = False
            if row == 0: down = True
        return ''.join(rows)
