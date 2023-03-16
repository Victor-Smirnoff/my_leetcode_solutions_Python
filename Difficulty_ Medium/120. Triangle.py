# https://leetcode.com/problems/triangle/
# 120. Triangle
# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
# Example 1:
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

class Solution:
    def minimumTotal(self, triangle):
        triangle = triangle[::-1]

        for i in range(len(triangle) - 1):
            for j in range(len(triangle[i]) - 1):
                if triangle[i][j] < triangle[i][j + 1]:
                    triangle[i + 1][j] += triangle[i][j]
                else:
                    triangle[i + 1][j] += triangle[i][j + 1]

        return triangle[-1][-1]
