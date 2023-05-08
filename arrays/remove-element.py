class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0 , len(nums) - 1
        while l <= r:
            # print(l, r, nums)
            if nums[r] == val:
                nums[r] = '_'
                r -= 1
            elif nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
            else:
                l += 1
        return r + 1
