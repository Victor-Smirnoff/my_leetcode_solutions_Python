# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/
# 1190. Reverse Substrings Between Each Pair of Parentheses
# You are given a string s that consists of lower case English letters and brackets.
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
# Your result should not contain any brackets.
# Example 1:
# Input: s = "(abcd)"
# Output: "dcba"
# Example 2:
# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.
# Example 3:
# Input: s = "(ed(et(oc))el)"
# Output: "leetcode"
# Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.

class Solution:
    def reverseParentheses(self, s):
        left = []

        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
            else:
                if s[i] == ')':
                    temp = s[left[-1]:i + 1]
                    s = s[:left[-1]] + temp[::-1] + s[i + 1:]
                    del left[-1]

        res = ''
        for i in range(len(s)):
            if s[i] != '(' and s[i] != ')':
                res += s[i]

        return res
