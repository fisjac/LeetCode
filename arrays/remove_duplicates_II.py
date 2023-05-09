class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 1, 1
        counts = {}
        counts[nums[0]] = 1
        while right < len(nums):
            counts[nums[left]] = counts.get(nums[left],0) + 1

            if type(nums[left]) != str and counts[nums[left]] <= 2 and nums[left] >= nums[left - 1]:
                left += 1
                right += 1
            else:
                if counts.get(nums[right], 0) < 2:
                    nums[left] = nums[right]
                    nums[right] = '_'
                    counts[nums[left]] = counts.get(nums[left],0) + 1
                    left += 1
                    right += 1
                else:
                    right += 1
        return left
