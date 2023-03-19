# https://leetcode.com/problems/longest-valid-parentheses/description/
# 32. Longest Valid Parentheses
# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
# substring.
# Example 1:
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:
# Input: s = ""
# Output: 0

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        _stack = [-1]
        max_lenght = 0
        for i in range(len(s)):
            if s[i] == '(':
                _stack.append(i)
                continue
            if s[i] == ')':
                if _stack:
                    _stack.pop()
                    if _stack:
                        x = _stack[-1]
                        if i - x > max_lenght:
                            max_lenght = i - x
                            continue
                    if not _stack:
                        _stack.append(i)
        return max_lenght
