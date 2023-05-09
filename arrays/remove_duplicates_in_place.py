# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         k = len(nums)
#         if k == 1: return k

#         for i in range(len(nums)-1,0,-1):
#             # print(i, nums)
#             prev, current = nums[i-1],nums[i]
#             if current == prev:
#                 k -= 1
#                 for j in range(i,k):
#                     nums[j], nums[j+1] = nums[j+1], nums[j]
#                     # print(nums, k)
#         return k


# Better Solution:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right  = 1, 1

        while right < len(nums):
            if nums[right] != nums[right - 1]:
                nums[left] = nums[right]
                left += 1
                right += 1
            else:
                right += 1

        return left
