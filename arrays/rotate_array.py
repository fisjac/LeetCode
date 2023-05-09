class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotations = len(nums) - k % len(nums)

        for i in range(rotations):
            nums.append(nums[i])
        for i in range(rotations):
            nums.pop(0)
