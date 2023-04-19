from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def inBounds(row,col):
            rowInbounds = row >= 0 and row < len(grid)
            colInbounds = col >= 0 and col < len(grid[0])
            return rowInbounds and colInbounds

        oranges = set()
        rotten_start = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1: oranges.add((row,col))
                if grid[row][col] == 2:
                    oranges.add((row,col))
                    rotten_start.append((row,col))

        directions = [(0,1), (1,0),(-1,0),(0,-1)]
        queue = deque()
        for orange in rotten_start:
            (row, col) = orange
            queue.append((orange,0))
            grid[row][col] = 1

        max_minutes = 0

        while len(queue) > 0:
            (node, minutes) = queue.popleft()
            (row, col) = node
            # print(node)
            if not inBounds(row,col):
                continue
            if grid[row][col] == 1:
                [queue.append(((row+row_delta,col+col_delta), minutes + 1)) for (row_delta, col_delta) in directions]
                grid[row][col] = 2
                oranges.remove((row,col))
                max_minutes = max(max_minutes, minutes)
                # print('minutes now:', max_minutes)

        # print(oranges)
        if len(oranges) > 0: return -1
        return max_minutes
