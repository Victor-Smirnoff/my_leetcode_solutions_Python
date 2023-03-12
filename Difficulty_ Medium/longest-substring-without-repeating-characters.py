# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest 
# substring without repeating characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s):
        res = []

        for i in range(len(s)):
            tmp = ''
            for j in range(i, len(s)):
                if s[j] not in tmp:
                    tmp += s[j]
                    res.append(tmp)
                    continue
                else:
                    res.append(tmp)
                    break

        return max([int(len(x)) for x in res]) if s else 0
