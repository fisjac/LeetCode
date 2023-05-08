class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1, idx2 = m - 1, n - 1
        pointer = len(nums1) - 1
        while pointer >= 0 and idx2 >= 0:
            # print(idx1, idx2, pointer, nums1, nums2)
            if nums1[idx1] < nums2[idx2] or idx1 < 0:
                nums1[pointer] = nums2[idx2]
                idx2 -= 1
                pointer -= 1
            else:
                nums1[idx1], nums1[pointer] = nums1[pointer], nums1[idx1]
                idx1 -= 1
                pointer -= 1
