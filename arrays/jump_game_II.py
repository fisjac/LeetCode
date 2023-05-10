class Solution:
    def jump(self, nums: List[int]) -> int:
        def checkReach(prev_reach, curr_reach):
            new_reach = curr_reach
            for step in range(prev_reach, curr_reach + 1):   # check max reach from available
                new_reach = max(new_reach, nums[step] + step)
            return curr_reach, new_reach

        if len(nums) == 1: return 0
        jumps = 0
        prev_reach, curr_reach = 0, 0
        while curr_reach < len(nums) - 1:
            prev_reach, curr_reach = checkReach(prev_reach, curr_reach)
            if prev_reach == curr_reach: return False
            jumps += 1
        return jumps
