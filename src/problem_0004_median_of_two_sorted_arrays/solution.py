from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        l = len(nums)
        if l % 2 == 0:
            return (nums[l // 2] + nums[l // 2 - 1]) / 2
        else:
            return nums[l // 2]
