class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_counts = [0,0,0] #initialize buckets
        for i in range(len(nums)):
            color_counts[nums[i]] += 1

        current_color = 0
        for i in range(len(nums)): # for each num in the nums
            while color_counts[current_color] == 0:
                current_color += 1
            nums[i] = current_color
            color_counts[current_color] -= 1
