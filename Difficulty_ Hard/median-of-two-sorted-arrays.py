#  https://leetcode.com/problems/median-of-two-sorted-arrays/
#  4. Median of Two Sorted Arrays
#  Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#  The overall run time complexity should be O(log (m+n)).


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = sorted(nums1 + nums2)
        return num[int(len(num) / 2)] if len(num) % 2 != 0 else (num[int(len(num) / 2) - 1] + num[int(len(num) / 2)]) / 2
