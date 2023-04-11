class Solution:
    def isValidSection(self, section: List[str]) -> bool:
        numbers_seen = set() # initialize hashset
        # print(section)
        for num in section: # iterate through list
            if num != '.' and num in numbers_seen: # if is a number and number exists
                return False # invalid
            else:
                numbers_seen.add(num)# add numbers to hashmap
        return True # return true



    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(9):
            # print('------rows------')
            if not self.isValidSection(board[i]):
                return False

        # check columns
            # print('------cols------')
            if not self.isValidSection([board[j][i] for j in range(9)]):
                return False

        # check squares
            # print('------squares------')
            box_row = (i // 3)*3
            box_col = (i % 3)*3
            if not self.isValidSection([board[box_row + (j // 3)][box_col + (j % 3)] for j in range(9)]):
                return False

        return True
