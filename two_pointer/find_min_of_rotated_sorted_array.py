class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums) - 1
        if len(nums) == 1: return nums[0]
        while l < r:
            mid = l + (r - l) // 2
            # print(nums[l],nums[mid],nums[r])
            if nums[l] <= nums[mid] < nums[r]:
                return nums[l]
            elif nums[mid] >= nums[l] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
