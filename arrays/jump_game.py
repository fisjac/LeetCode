class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        jumps_left = nums[0]
        i = 0
        while jumps_left > 0:
            i += 1
            if i == len(nums) - 1: return True
            jumps_left -= 1
            if nums[i] > jumps_left:
                jumps_left = nums[i]
        return False
