# https://leetcode.com/problems/counting-bits/description/
# 338. Counting Bits
# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
# Example 1:
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

class Solution:
    def countBits(self, n):
        def get_num(num, base=2):
            res = ''
            while num > 0:
                digit = num % base
                res += str(digit)
                num //= base
            return res[::-1]

        tmp_lst = list(map(get_num, list(range(n + 1))))
        return [tmp_lst[i].count('1') for i in range(len(tmp_lst))]
