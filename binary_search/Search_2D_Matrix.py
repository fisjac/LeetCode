class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outer_left, outer_right = 0, len(matrix) - 1 # initial l / r pointers at 0, m-1 for outer array
        inner_left, inner_right = 0, len(matrix[0]) - 1 # set inner pointers l / r at 0, n - 1
        while outer_left <= outer_right: # while l < r
            outer_mid = (outer_right + outer_left) // 2     # set mid to middle subarray
            subarray = matrix[outer_mid]
            # print(subarray)
            if target >= subarray[inner_left] and target <= subarray[inner_right]: # check if target is between first and last
                while inner_left <= inner_right:    # while inner_left < inner_right
                    inner_mid = (inner_left + inner_right) // 2 # set inner_mid
                    # print(subarray[inner_left], subarray[inner_mid], subarray[inner_right])
                    if target > subarray[inner_mid]: inner_left = inner_mid + 1# if target > inner_mid reset inner_left/ inverse for less than
                    elif target < subarray[inner_mid]: inner_right = inner_mid - 1  # if mid == target, return true
                    if target == subarray[inner_mid]: return True
            else:
                if target < subarray[inner_left]: outer_right = outer_mid - 1 # if target is greater, set left = mid + 1; if less than set right = mid - 1
                else: outer_left = outer_mid + 1
        return False
