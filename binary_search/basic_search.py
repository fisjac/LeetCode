class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1 # initialize left and right pointers
        while l <= r: # while l < r
            mid = l + ((r-l) // 2)    # create mid
            print(l,mid,r)
            if nums[mid] == target: return mid    # if target == mid return mid
            if target > nums[mid]: l = mid+1 # if target > mid shift left to mid + 1
            if target < nums[mid]: r = mid - 1   # if target < mid shift right to mid - 1
        return -1
