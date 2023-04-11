# https://leetcode.com/problems/minimum-size-subarray-sum/


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = sum(nums)

        min_len = 0
        if cur_sum < target:
            return 0
        else:
            nums.sort(reverse = True)
            while target <= cur_sum:
                cur_sum -= nums.pop()
                print(cur_sum)
            return len(nums) + 1
