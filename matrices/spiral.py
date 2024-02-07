class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        total_cells = m * n

        right,left,top,bottom = 0,0,0,0
        col_layer = 0
        direction = 0

        i, j = 0,0
        while len(res) < total_cells:
            # print(res)
            match(direction):
                case 0:
                    if j == n - 1 - right:
                        top += 1
                        direction += 1
                    else:
                        res.append(matrix[i][j])
                        j += 1
                case 1:
                    if i == m - 1 - bottom:
                        right += 1
                        direction += 1
                    else:
                        res.append(matrix[i][j])
                        i += 1
                case 2:
                    if j == left:
                        bottom += 1
                        direction += 1
                    else:
                        res.append(matrix[i][j])
                        j -= 1
                case 3:
                    if i == top:
                        left += 1
                        direction = 0
                    else:
                        res.append(matrix[i][j])
                        i -= 1
        return res
