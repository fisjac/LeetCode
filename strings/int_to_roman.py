class Solution:
    def intToRoman(self, num: int) -> str:
        zeroes = {
            0: {1:'I', 5:'V'},
            1: {1:'X', 5:'L'},
            2: {1:'C', 5:'D'},
            3: {1:'M'},
        }

        num_zeroes = len(str(num))
        res = ''
        for digit in str(num):
            char_to_add = ''
            num_zeroes -= 1
            if digit == '9':
                char_to_add = zeroes[num_zeroes][1] + zeroes[num_zeroes+1][1]
            elif digit == '4':
                char_to_add = zeroes[num_zeroes][1] + zeroes[num_zeroes][5]
            elif int(digit) >= 5:
                char_to_add = zeroes[num_zeroes][5] + ''.join([zeroes[num_zeroes][1] for _ in range(int(digit) % 5)])
            else:
                char_to_add = ''.join([zeroes[num_zeroes][1] for _ in range(int(digit))])
            res += char_to_add
        return res
