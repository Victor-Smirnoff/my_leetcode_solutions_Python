# https://leetcode.com/problems/reverse-integer/
# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Example 1:
# Input: x = 123
# Output: 321
# Example 2:
# Input: x = -123
# Output: -321
# Example 3:
# Input: x = 120
# Output: 21

class Solution:
    def reverse(self, x: int) -> int:
        acceptable_range = range(-2147483648, 2147483648 - 1)
        x = int('-' + str(x)[1:][::-1]) if '-' in str(x) else int(str(x)[::-1])
        return x if x in acceptable_range else 0
