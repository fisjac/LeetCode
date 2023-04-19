from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def inBounds(row,col):
            rowInbounds = row >= 0 and row < len(mat)
            colInbounds = col >= 0 and col < len(mat[0])
            return rowInbounds and colInbounds

        starting_zeroes = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    starting_zeroes.append((row,col))
                else:
                    mat[row][col] = 10 ** 4

        directions = [(0,1), (1,0),(-1,0),(0,-1)]
        def _BFS(coords):
            queue = deque()
            queue.append((coords, 0))
            visited = set()
            while len(queue) > 0:
                (coords, dist) = queue.popleft()
                visited.add(coords)
                # print('-----',coords, dist, visited,queue,'------')

                # if not zero and valid
                for (row_delta, col_delta) in directions:
                    new_row, new_col = row + row_delta, col + col_delta
                    # print('at',(row,col),'looking at:',(new_row,new_col))
                    if (new_row, new_col) in visited: continue
                    if not inBounds(new_row,new_col): continue
                    if mat[new_row][new_col] != 0:
                        # print('adding:',(new_row,new_col))
                        mat[row][col] = min(dist, mat[row][col]) # assign new matrix value to coord
                        queue.append(((new_row,new_col), dist + 1))
        [_BFS(coords) for coords in starting_zeroes]
        # _BFS((0,1))
        return mat
