class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l, r = 0, len(height) - 1
        ceil = 0
        while l < r:
            current_ceil = min(height[l], height[r])
            ceil = max(ceil, current_ceil)
            if height[l] <= height[r]:
                l += 1
                total += max(ceil - height[l], 0)
            else:
                r -= 1
                total += max(ceil - height[r], 0)
        return total
