# https://leetcode.com/problems/container-with-most-water/


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        while (left < right):
            current_area = min(height[left], height[right]) * (right-left)
            if current_area > max_area: # if area greater,
                max_area = current_area # record area

            if height[left] < height[right]:  #increment logic
                left += 1
            else:
                right -= 1
        return max_area
