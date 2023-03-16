# https://leetcode.com/problems/container-with-most-water/
# 11. Container With Most Water
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, rigth = 0, len(height) - 1
        while rigth > left:
            h_max = max(height[left], height[rigth])
            x = min(height[left], height[rigth]) * (rigth - left)
            if x > res:
                res = x
            if height[left] <= height[rigth]:
                left += 1
            elif height[left] > height[rigth]:
                rigth -= 1

        return res
