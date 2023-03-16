# https://leetcode.com/problems/3sum/
# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

class Solution:
    def threeSum(self, nums):
        size, result = len(nums), set()
        nums.sort()

        for idx, num in enumerate(nums[:size - 2]):
            target, left, right = - num, idx + 1, size - 1

            while left < right:
                if target == (nums[left] + nums[right]):
                    result |= {(num, nums[left], nums[right])}
                    left, right = left + 1, right - 1
                    continue
                if nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

        return sorted(result)
